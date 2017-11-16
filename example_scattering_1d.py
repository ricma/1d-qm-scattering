"""
Use a shooting method for a simple scattering system
"""
from __future__ import division, print_function

import numpy as np
from scipy.linalg import eig_banded
import multiprocessing
import matplotlib.pyplot as plt
import contextlib
import collections
from functools import reduce


def lorentz(x, x_0=0, s=1):
    """
    https://en.wikipedia.org/wiki/Spectral_line_shape
    """
    y = 2 * (x - x_0) / s
    return 1 / (y**2 + 1)


def gauss(x, x_0=0, s=1):
    """
    https://en.wikipedia.org/wiki/Spectral_line_shape
    """
    y = (x - x_0) / s
    return np.exp(-y**2 / 2) / s


def V(x, *args, **kwargs):
    """
    potential to use
    """
    l = args[0]
    #return lorentz(x, 0, 5 * l) - 1.1 * lorentz(x, 0, 2.5 * l)
    return (0.2 * (gauss(x, -1.5, 3 * l) + gauss(x, 1.5, 3 * l))
            - 0.5 * gauss(x, 0, 6.1 * l) ** 2)
    # For testing:
    # return np.zeros_like(x)


def get_scattering_state(E, x, pot, hbareff):
    """
    Use the shooting method to get |psi>

    Note: As it is a scattering state, every psi is a solution

    See Also
    --------
    [[example_scattering_1d.org]]: file with details
    """
    # For x at -L_max we assume
    # psi = exp(i k x) = exp(-i k L_max) and
    # d psi / dx = i k * psi
    N = len(x)
    dx = x.ptp() / (N - 1)
    z = hbareff ** 2 / 2 / dx ** 2

    # estimate the wavelength on the left and right (in indices)
    n_wavelengths = 4
    # this is k * dx
    k_left_0_dx = np.sqrt((E - pot[0]) / z)
    k_right_0_dx = np.sqrt((E - pot[-1]) / z)

    # Note: We need the min condition in case E is too small and the
    # wavelength diverges
    idx_wavelength_l = min(N // 20, int(np.ceil(
        2 * np.pi * n_wavelengths / k_left_0_dx)))
    idx_wavelength_r = min(N // 20, int(np.ceil(
        2 * np.pi * n_wavelengths / k_right_0_dx)))

    # we assume the potential is constant over these ranges
    k_left = np.sqrt((E - pot[:idx_wavelength_l]) / z) / dx
    k_right = np.sqrt((E - pot[-idx_wavelength_r:]) / z) / dx

    offset = np.exp(-1j * k_right[-1] * x[-1])

    # We only check on a fraction of the array -- it suffices.
    # We use the arrays for plotting outside
    np.testing.assert_array_less(
        k_left[:len(k_left) // 10].std(), 5e-2,
        err_msg="potential not constant at the left: k_left={0}".format(
            list(k_left[:len(k_left)])))
    np.testing.assert_array_less(
        k_right[:len(k_right) // 10].std(), 5e-2,
        err_msg="potential not constant at the right")

    def iterate(psi_ip1, psi_i, V_ip1):
        """
        get psi_{i + 2} = psi_ip2 from psi_ip1 and psi_1
        """
        return (2 - (E - V_ip1) / z) * psi_ip1 - psi_i

    def get_psi(r):
        """
        calculate the transmission amplitude from the reflection
        """
        # now we can construct the rest of the function
        psi = np.empty(N, dtype=np.complex)
        psi[0] = offset * (
            np.exp(1j * k_left[0] * x[0]) +
            r * np.exp(-1j * k_left[0] * x[0]))
        psi[1] = offset * (
            np.exp(1j * k_left[0] * (x[0] + dx)) +
            r * np.exp(-1j * k_left[0] * (x[0] + dx)))

        for i in range(N - 2):
            psi[i + 2] = iterate(psi[i + 1], psi[i], pot[i + 1])

        return psi

    transfer_M = reduce(
        lambda M, V_ip1: np.dot(
            np.array([[0, 1], [
                iterate(0, 1, 0),
                iterate(1, 0, V_ip1)]]), M),
        pot[1:-1], np.eye(2))

    # create the scattering matrix
    y_1 = np.exp(-1j * k_left_0_dx)
    y_2 = np.exp(-1j * k_right_0_dx)
    Y_1 = np.exp(1j * k_left_0_dx * x[0] / dx)
    Y_2 = np.exp(1j * k_right_0_dx * x[-1] / dx)

    g_1 = Y_2 * np.array([y_2, 1])
    g_2 = 1 / Y_2 * np.array([1 / y_2, 1])
    M_d_1 = np.dot(transfer_M, Y_1 * np.array([1, 1 / y_1]))
    M_d_2 = np.dot(transfer_M, 1 / Y_1 * np.array([1, y_1]))

    S = np.dot(
        np.linalg.inv(np.array([
            [-M_d_2[0], g_1[0]],
            [-M_d_2[1], g_1[1]]])),
        np.array([
            [M_d_1[0], g_2[0]],
            [M_d_1[1], g_2[1]]]))

    # we can re-cast the problem in terms of the the transfer matrix:
    c = np.dot(transfer_M, np.array([1, np.exp(1j * k_left_0_dx)])) * (
        np.exp(1j * k_left[0] * x[0])) * offset
    d = np.exp(-1j * k_left[0] * x[0]) * offset * np.dot(
        transfer_M, np.array([1, np.exp(-1j * k_left_0_dx)]))
    g = np.array([np.exp(-1j * k_right_0_dx), 1])
    # we now have to solve
    # c + r * d - t * g = 0
    # and |r|^2 + |t|^2 = 1

    A = np.linalg.inv(np.array([d, g]).T)
    amplitudes = np.dot(A, c)
    r, t = amplitudes

    # The scattering state corresponds to
    # a1 = 1, b1 = r, a2 = 0, b2 = t so
    # r = (S * [1, 0]^T)[0] = S[0, 0]
    psi = get_psi(S[0, 0])

    # Norm such that the integral over the visible region is 1
    # Note: Commented out as this has the downside that we cannot see
    # the incident wave if we hit a resonance --> the resonance is just
    # to efficiently coupled and gets blown up.
    # c_norm = dx * np.sum(np.abs(psi)**2)
    # psi = psi / np.sqrt(c_norm)

    # we norm such that the part of the plane-wave component has a
    # maximum of one
    # Note: The asymptotic scattering function is given by
    # psi = offset * ( (1 + r) cos(k x) + i (1 - r) sin(k x))
    # (Note that r is complex itself)
    # psi = offset * (e^ikx + |r| e^i(delta_r - kx))
    # but we can get a good bound by:
    psi /= np.abs(1 + np.abs(r))

    return S, psi, t, r, k_left, k_right


class QuantumSystem(object):
    """
    Define the necessary parameters
    """
    def __init__(self, hbareff=0.1, N=2500, L_max=5,
                 potential_args=(0.2, )):
        """
        Set up the scattering state
        """
        self.hbareff = hbareff
        self.N = N
        self.potential_args = potential_args

        # first plot the potential
        self.L_max = L_max
        self.x, self.dx = np.linspace(
            -L_max, L_max, N, retstep=True)
        self.pot = self.V(self.x, *potential_args)

    def V(self, *args):
        """
        return the potential in use
        """
        return V(*args)

    def plot_psi(self, psi, E):
        """
        scale the plot of the wavefunction

        The prefactor is just for visibility
        """
        return E + 0.1 * np.abs(psi) ** 2


class ClosedSystem(QuantumSystem):
    """
    Diagonalize the problem using Dirichlet conditions
    """
    def __init__(self, *args, **kwargs):
        super(ClosedSystem, self).__init__(*args, **kwargs)

        # adjust self.x to account for the maxima of the potential
        dpot = np.diff(self.pot)
        idx_left = np.nonzero(dpot < 0)[0][0] + 1
        idx_right = np.nonzero(dpot > 0)[0][-1]
        self.x, self.dx = np.linspace(
            self.x[idx_left], self.x[idx_right], self.N, retstep=True)
        self.pot = self.V(self.x, *self.potential_args)

    def create_H_banded(self):
        """
        create banded matrix for diagonalization
        """
        H_banded = np.zeros((2, self.N), dtype=float)
        z = self.hbareff**2 / (2 * self.dx ** 2)

        # main diagonal = 1st band (in lower storage)
        H_banded[0, :] = 2 * z + self.pot
        H_banded[1, :-1] = - z

        return H_banded

    def get_evals_evecs(self):
        """
        get bound states
        """
        H = self.create_H_banded()
        evals, evecs = eig_banded(
            H, lower=True, select="v",
            select_range=(self.pot.min(),
                          self.pot.max()))
        # fix the eigenvector norm to the position space integral
        evecs /= np.sqrt(self.dx)
        return evals, evecs

    def plot_evecs_to(self, ax):
        """
        plot all found eigenvectors to ax
        """
        evals, evecs = self.get_evals_evecs()

        for eigval, evec in zip(evals, evecs.T):
            ax.plot(
                self.x, self.plot_psi(evec, eigval),
                color="g", alpha=0.4)


class ScatteringState(QuantumSystem):
    """
    combine the current scattering info
    """
    def get_state(self, E):
        """
        calculate the scattering state

        This is the state incident from the left
        with no component entering from the right
        """
        S, psi, t, r, k_l, k_r = get_scattering_state(
            E, self.x, self.pot,
            self.hbareff)

        return S, psi, t, r, k_l, k_r

    def get_S(self, E):
        """
        calculate S matrix
        """
        S, psi, t, r, k_l, k_r = get_scattering_state(
            E, self.x, self.pot,
            self.hbareff)
        return S

    def plot_state_at_E(self, ax, ax_phase, ax_trans, E):
        """
        plot psi to ax, E to ax_phase
        """
        S, psi, t, r, k_l, k_r = self.get_state(E)
        delta = np.angle(t)

        try:
            psi_plot_baseline = self.psi_plot_baseline
        except AttributeError:
            self.psi_plot_baseline = ax.plot(
                self.x, self.plot_psi(np.zeros_like(self.x), E),
                color="k", lw=0.5, alpha=0.5)[0]
        else:
            psi_plot_baseline.set_ydata(
                self.plot_psi(np.zeros_like(self.x), E))

        try:
            psi_plot = self.psi_plot
        except AttributeError:
            self.psi_plot = ax.plot(
                self.x, self.plot_psi(psi, E), color="r")[0]
        else:
            psi_plot.set_ydata(self.plot_psi(psi, E))

        # also plot a comparison for the phase shift
        where = slice(len(k_l))
        psi_in = np.exp(1j * k_l * self.x[where])
        try:
            psi_in_plot = self.psi_in_plot
        except AttributeError:
            self.psi_in_plot = ax.plot(
                self.x[where], self.plot_psi(psi_in[where], E),
                color="b", alpha=0.3)[0]
        else:
            psi_in_plot.set_data(
                self.x[where], self.plot_psi(psi_in[where], E))

        where = slice(-len(k_r), None)
        psi_out = np.exp(1j * k_r * self.x[where] + 1j * delta)
        try:
            psi_out_plot = self.psi_out_plot
        except AttributeError:
            self.psi_out_plot = ax.plot(
                self.x[where], self.plot_psi(psi_out[where], E),
                color="g", alpha=0.3)[0]
        else:
            psi_out_plot.set_data(
                self.x[where],
                self.plot_psi(psi_out[where], E))

        # add a straight line at the phase plot
        try:
            E_in_phase = self.E_in_phase
        except AttributeError:
            self.E_in_phase = ax_phase.axvline(
                E, color="k", lw=0.5, alpha=0.5)
        else:
            E_in_phase.set_xdata([E, E])

        # add a straight line at the phase plot
        try:
            E_in_trans = self.E_in_trans
        except AttributeError:
            self.E_in_trans = ax_trans.axvline(
                E, color="k", lw=0.5, alpha=0.5)
        else:
            E_in_trans.set_xdata([E, E])


class Heff(QuantumSystem):
    """
    Holds the closed sys and the scattering state
    """
    def __init__(self, *args, **kwargs):
        self.scat = ScatteringState(*args, **kwargs)
        self.Hsys = ClosedSystem(*args, **kwargs)
        super(Heff, self).__init__(*args, **kwargs)

    def get_state(self, *args, **kwargs):
        """
        pass on to the scattering code
        """
        return self.scat.get_state(*args, **kwargs)


    def plot_state_at_E(self, *args, **kwargs):
        """
        pass on to the scattering code
        """
        return self.scat.plot_state_at_E(*args, **kwargs)

    def plot_evecs_to(self, *args, **kwargs):
        """
        pass on to the closed system
        """
        return self.Hsys.plot_evecs_to(*args, **kwargs)


@contextlib.contextmanager
def pool(*args, **kwargs):
    yield multiprocessing.Pool(*args, **kwargs)


def get_S_t_r(args):
    """
    return all things necessary for plotting
    """
    scatstate, E = args
    S, _, t, r = scatstate.get_state(E)[:4]
    return np.concatenate([S.flatten(), np.array([t, r])])


def main(afterwards=plt.show, savefig=False):
    """
    Make an example plot
    """
    scatstate = Heff(
        hbareff=0.2, N=3500, L_max=5,
        potential_args=(0.2, ))

    # Note: The lower lying states are too close to E=0
    # for the choosem L_max!
    E = 0.122698680068     # 3rd  (2 zeros)
    E = 0.2514             # 4th  (3 zeros)
    # --- pot maximum: 0.2692 ---
    E = 0.3815             # 5th  (4 zeros)

    N_E = 5000
    E_delta = np.linspace(
        scatstate.pot[0] + 0.001, 2, N_E)

    description = "_".join([
        "E_min={0:1.7f}".format(E_delta.min()),
        "E_max={0}".format(E_delta.max()),
        "E_N={0}".format(N_E),
        "hbar_{0}".format(scatstate.hbareff),
        "N_{0}".format(scatstate.N),
        "L_max={0}".format(scatstate.L_max),
        "potential={0}".format(scatstate.potential_args[0])])

    cache = "example_scattering_1d_cached_values{desc}.dat".format(
        desc=description)
    try:
        tr_amp = np.memmap(cache, mode="r", dtype=complex)
    except IOError:
        print("Calculating ... ({0})".format(cache))
        with pool() as p:
            tr_amp = np.array(p.map(
                get_S_t_r, [(scatstate, E_) for E_ in E_delta]))

        tr_amp.tofile(cache)
        print("Wrote {0}".format(cache))
    else:
        tr_amp = tr_amp.reshape((N_E, -1))
        print("Read {0}".format(cache))

    S = tr_amp[:, :4].reshape(-1, 2, 2)

    fig = plt.figure(1)
    ax = fig.add_subplot(121)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$E$ / $|\psi|^{2}$")
    ax.plot(scatstate.x, scatstate.pot,
            "k-")
    ax.plot(scatstate.x, np.zeros_like(scatstate.x),
            color="k", lw=0.5, alpha=0.5)
    scatstate.plot_evecs_to(ax)
    ax.set_ylim(min(-.1, 1.1 * scatstate.pot.min()),
                max(E + 1, 1.1 * scatstate.pot.max()))

    ax_phase = fig.add_subplot(222)
    ax_phase.set_xlabel(r"$E$")
    ax_phase.set_ylabel(r"$\delta_t$ / $\delta_r$")
    phases = np.angle(S[:, 1, 0])
    where = E_delta > 0.02
    phases[where] = np.unwrap(phases[where])
    ax_phase.plot(E_delta, phases,
                  "b-", lw=3, marker=".", alpha=0.5)
    phases = np.angle(S[:, 0, 0])
    phases[where] = np.unwrap(phases[where])
    ax_phase.plot(E_delta, phases,
                  "r-", lw=3, marker=".", alpha=0.5)

    ax_trans = fig.add_subplot(224, sharex=ax_phase)
    ax_trans.set_xlabel(r"$E$")
    ax_trans.set_ylabel(r"$|t|^2$, $|r|^2$")
    ax_trans.plot(E_delta, np.abs(S[:, 1, 0]) ** 2, "b-", label=r"$T$")
    ax_trans.plot(E_delta, np.abs(S[:, 0, 0]) ** 2, "r-", label=r"$R$")

    # mark the potential maximum
    ax_phase.axvline(scatstate.pot.max(), color="k", ls="-")
    ax_trans.axvline(scatstate.pot.max(), color="k", ls="-")

    # get a wave function
    scatstate.plot_state_at_E(ax, ax_phase, ax_trans, E)
    ax_trans.legend(loc="center right")
    ax_trans.set_xlim(0.1, 0.55)
    ax_trans.set_ylim(-0.01, 1.01)

    def set_energy_from_mouse(event):
        if plt.get_current_fig_manager().toolbar.mode != '':
            return
        if event.button != 1:
            return
        if event.inaxes is ax:
            E = event.ydata
        elif event.inaxes in [ax_phase, ax_trans]:
            E = event.xdata
        else:
            return
        set_energy(E)

    def set_energy_from_key(event):
        if event.inaxes is ax:
            step = np.ptp(event.inaxes.get_ylim()) / 50
            if event.key in ["up"]:
                E = set_energy.current_E + step
            elif event.key in ["down"]:
                E = set_energy.current_E - step
            else:
                return
        elif event.inaxes in [ax_phase, ax_trans]:
            step = np.ptp(event.inaxes.get_xlim()) / 50
            if event.key == ";":
                E = set_energy.current_E + step
            elif event.key == "j":
                E = set_energy.current_E - step
            else:
                return
        else:
            return
        set_energy(E)

    def set_energy(E):
        set_energy.current_E = E

        print("Setting E={0}".format(E))
        scatstate.plot_state_at_E(ax, ax_phase, ax_trans, E)
        plt.draw()

    set_energy.current_E = E

    fig.subplots_adjust(wspace=0.30, right=0.95)
    plt.connect('button_press_event', set_energy_from_mouse)
    plt.connect('key_press_event', set_energy_from_key)

    if savefig:
        filename = "./figures/example_scattering_1d.svg"
        fig.savefig(filename, transparent=True)
        print("Wrote {0}".format(filename))

    if isinstance(afterwards, collections.Callable):
        afterwards()


if __name__ == "__main__":

    main(savefig=False)
