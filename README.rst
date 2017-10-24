    :Author: mrichter



Discretization
--------------

We use :math:`\mathrm{d}^2 \psi / \mathrm{d}x^2 = \left(\psi_{i+1} - 2
  \psi_i + \psi_{i-1}\right) / \Delta x^2`
and define :math:`z = \hbar_\mathrm{eff}^2 / 2 / \Delta x^2`
such that the Hamiltonian reads


.. math::

    0 &= \frac{1}{z} (E - H) \psi \\
      &= \frac{1}{z} \left(E - V + z \Delta x^2 \partial^2 / \partial x^2\right) \psi \\
      &= \left(\begin{array}{c}
      \vdots\\
      \psi_{i+1} + \left(\frac{E - V_i}{z} - 2\right) \psi_i + \psi_{i-1}\\
      \vdots \end{array}\right)


and therefore:


.. math::

    \psi_{i+2} = \left(2 - \frac{E - V_{i+1}}{z}\right) \psi_{i+1} - \psi_i

Transfer Matrix
---------------

This allows to write a transfer matrix :math:`M` from
:math:`(\psi_{i}, \psi_{i+1}) \to (\psi_{i+1}, \psi_{i+2})`
as


.. math::

    \left(\begin{array}{c}
          \psi_{i+1} \\
          \psi_{i+2}
        \end{array}\right)
        &=
        M_{i+1}
        \left(\begin{array}{c}
          \psi_{i} \\
          \psi_{i+1}
        \end{array}\right)
        =
        \left(\begin{array}{cc}
          0 & 1 \\
          -1 & 2 - \frac{E - V_{i+1}}{z}
        \end{array}\right)
        \left(\begin{array}{c}
          \psi_{i} \\
          \psi_{i+1}
        \end{array}\right)


and


.. math::

    M = \prod\limits_{2}^{N-1} M_{N - i}


connecting the first two and the last two elements of :math:`\psi`:


.. math::

    \left(\begin{array}{c}
          \psi_{N - 2} \\
          \psi_{N - 1}
        \end{array}\right)
        &=
        M
        \left(\begin{array}{c}
          \psi_{0} \\
          \psi_{1}
        \end{array}\right)

Transmission and Reflection
---------------------------

These are linked to transmission and reflection via:


.. math::

    \psi_0 &= c \cdot \left(
        \mathrm{e}^{\mathrm{i} k x_0} +
        r \mathrm{e}^{-\mathrm{i} k x_0}\right) \\
      \psi_1 &= c \cdot \left(
        \mathrm{e}^{\mathrm{i} k (x_0 + \Delta x)} +
        r \mathrm{e}^{-\mathrm{i} k (x_0 + \Delta x)}\right) \\
      \psi_{N-1} &= c \cdot t \mathrm{e}^{\mathrm{i}kx_{N-1}}\\
      \psi_{N-2} &= c \cdot t \mathrm{e}^{\mathrm{i}k(x_{N-1} - \Delta x)}


Choosing the global phase such that we can compare the phases at
:math:`x_{N-1}`, i.e. :math:`c = \mathrm{e}^{-\mathrm{i}kx_{N-1}}`, we get
with


.. math::

    y &:= \mathrm{e}^{-\mathrm{i}k \Delta x} \\
        Y &:= c \cdot \mathrm{e}^{\mathrm{i}k x_0} =
        \mathrm{e}^{\mathrm{i}(k_l x_0 - k_r x_{N-1})}\\
        Y'&:= c \cdot \mathrm{e}^{-\mathrm{i}k x_0} =
        \mathrm{e}^{\mathrm{i}(-k_l x_0 - k_r x_{N-1})}


we have


.. math::

    t \left(\begin{array}{c} y \\ 1 \end{array}\right)
      & = M \left(\begin{array}{c} Y \\ Y/y \end{array}\right) +
      r \cdot M \left(\begin{array}{c} Y' \\ Y'/y \end{array}\right)


which in the code below are called
``t * g = c + r * d``, i.e.,


.. math::

    \vec{g} &:= \left(\begin{array}{c} y \\ 1 \end{array}\right) \\
      \vec{c} &:= Y / y M \cdot \vec{g}\\
      \vec{d} &:= Y' / y M \cdot \vec{g},


and which we can write as a linear system of equations
for :math:`r` and :math:`t`


.. math::

    \vec{c} = r\cdot \vec{d} - t \cdot \vec{g}


and we can rewrite this as


.. math::

    \left(\begin{array}{c} c_1 \\ c_2 \end{array}\right) =
      \left(\begin{array}{cc} d_1 & -g_1\\ d_2 & -g_2 \end{array}\right)
      \left(\begin{array}{c} r \\ t \end{array}\right)


and therefore


.. math::

    \left(\begin{array}{c} r \\ t \end{array}\right) =
      \left(\begin{array}{cc} d_1 & -g_1\\ d_2 & -g_2 \end{array}\right)^{-1}
      \left(\begin{array}{c} c_1 \\ c_2 \end{array}\right)

Scattering Matrix
~~~~~~~~~~~~~~~~~

Note that we can more generally define:


.. math::

    \psi_0 &=
         a_1 \mathrm{e}^{\mathrm{i} k_1 x_0} +
         b_1 \mathrm{e}^{-\mathrm{i} k_1 x_0} \\
       \psi_1 &=
         a_1 \mathrm{e}^{\mathrm{i} k_1 (x_0 + \Delta x)} +
         b_1 \mathrm{e}^{-\mathrm{i} k_1 (x_0 + \Delta x)} \\
       \psi_{N-2} &=
         b_2 \mathrm{e}^{\mathrm{i} k_2 (x_{N-1} - \Delta x)} +
         a_2 \mathrm{e}^{-\mathrm{i} k_2 (x_{N-1} - \Delta x)} \\
       \psi_{N-1} &=
         b_2 \mathrm{e}^{\mathrm{i} k_2 x_{N-1}} +
         a_2 \mathrm{e}^{-\mathrm{i} k_2 x_{N-1}} \\


where we this time explicitly differentiate between the :math:`k` values
on both sides: :math:`k_1` vs. :math:`k_2`. We use prefactors :math:`a_i` for
incoming and :math:`b_i` for outgoing components. Indices :math:`1` correspond to
left (:math:`x < 0`), indices :math:`2` to right (:math:`x > 0`).

With them the above becomes with
:math:`y_1 = \mathrm{e}^{-\mathrm{i}k_1 \Delta x}`,
:math:`y_2 = \mathrm{e}^{-\mathrm{i}k_2 \Delta x}`,
:math:`Y_1 = \mathrm{e}^{\mathrm{i}k_1 x_0}`, and
:math:`Y_2 = \mathrm{e}^{\mathrm{i}k_2 x_{N-1}}` using


.. math::

    \vec{d_1} &:= Y_1 \left(\begin{array}{c} 1 \\ 1/y_1 \end{array}\right)\\
       \vec{d_2} &:= Y_1^{-1} \left(\begin{array}{c} 1 \\ y_1 \end{array}\right)\\
       \vec{g_1} &:= Y_2 \left(\begin{array}{c} y_2 \\ 1 \end{array}\right)\\
       \vec{g_2} &:= Y_2^{-1} \left(\begin{array}{c} 1/y_2 \\ 1 \end{array}\right)


the following equation:


.. math::

    \left(\begin{array}{c}
           \psi_{N - 2} \\
           \psi_{N - 1}
         \end{array}\right)
         &=
         M
         \left(\begin{array}{c}
           \psi_{0} \\
           \psi_{1}
         \end{array}\right)\\
         b_2 \vec{g_1} + a_2 \vec{g_2} &= M \left(
         a_1 \vec{d_1} + b_1 \vec{d_2}
         \right)\\
         &= a_1 M\vec{d_1} + b_1 M\vec{d_2}


Such that we can map incoming to outgoing amplitudes


.. math::

    b_2 \vec{g}_1 - b_1 M\vec{d}_2 =
       a_1 M\vec{d}_1 - a_2\vec{g}_2


and therefore



.. math::

    \left(\begin{array}{cc}
       -(M\vec{d}_2)_1 & (\vec{g}_1)_1\\
       -(M\vec{d}_2)_2 & (\vec{g}_1)_2\\
       \end{array}\right)
       \vec{b} =
       \left(\begin{array}{cc}
       (M\vec{d}_1)_1 & (\vec{g}_2)_1\\
       (M\vec{d}_1)_2 & (\vec{g}_2)_2\\
       \end{array}\right)
       \vec{a}


hence



.. math::

    S =
       \left(\begin{array}{cc}
       -(M\vec{d}_2)_1 & (\vec{g}_1)_1\\
       -(M\vec{d}_2)_2 & (\vec{g}_1)_2\\
       \end{array}\right)^{-1}
       \left(\begin{array}{cc}
       (M\vec{d}_1)_1 & (\vec{g}_2)_1\\
       (M\vec{d}_1)_2 & (\vec{g}_2)_2\\
       \end{array}\right)

See Also
--------

`./example_scattering_1d. <./example_scattering_1d.>`_: org file with details
