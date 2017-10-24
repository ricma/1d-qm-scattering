

# Discretization

We use <img src="img/example_scattering_1d_23f8e90beeda6cd2c245c194fe3b355ca752cd71.png" alt="example_scattering_1d_23f8e90beeda6cd2c245c194fe3b355ca752cd71.png" />
and define <img src="img/example_scattering_1d_fecf8136ee41f1fa1efd0ec79a6eaf8a7775aac3.png" alt="example_scattering_1d_fecf8136ee41f1fa1efd0ec79a6eaf8a7775aac3.png" />
such that the Hamiltonian reads


<div class="figure">
<p><img src="img/example_scattering_1d_32b47cdc1ef542df3d403cd4d1642eb69be3c50e.png" alt="example_scattering_1d_32b47cdc1ef542df3d403cd4d1642eb69be3c50e.png" /></p>
</div>

and therefore:


<div class="figure">
<p><img src="img/example_scattering_1d_3c65bb62ed411618388c8409a80c027814fe86d8.png" alt="example_scattering_1d_3c65bb62ed411618388c8409a80c027814fe86d8.png" /></p>
</div>


# Transfer Matrix

This allows to write a transfer matrix <img src="img/example_scattering_1d_2c35f52ee9161be37ecdf2323e238bed1e748759.png" alt="example_scattering_1d_2c35f52ee9161be37ecdf2323e238bed1e748759.png" /> from
<img src="img/example_scattering_1d_ee4995121ca33b976157b03d35553a6a3fdf8112.png" alt="example_scattering_1d_ee4995121ca33b976157b03d35553a6a3fdf8112.png" />
as


<div class="figure">
<p><img src="img/example_scattering_1d_3fbdcb4066603da0023826f3ceebdb97a96b9933.png" alt="example_scattering_1d_3fbdcb4066603da0023826f3ceebdb97a96b9933.png" /></p>
</div>

and


<div class="figure">
<p><img src="img/example_scattering_1d_5e283ebba2f64da72ee0f3bd22238ea02dcd913a.png" alt="example_scattering_1d_5e283ebba2f64da72ee0f3bd22238ea02dcd913a.png" /></p>
</div>

connecting the first two and the last two elements of <img src="img/example_scattering_1d_d4d41339468db966b96739543dfeeaa6f34d9162.png" alt="example_scattering_1d_d4d41339468db966b96739543dfeeaa6f34d9162.png" />:


<div class="figure">
<p><img src="img/example_scattering_1d_c64cb3dc97ff6c8fd8d0b3ef8c1a0e172847ee4c.png" alt="example_scattering_1d_c64cb3dc97ff6c8fd8d0b3ef8c1a0e172847ee4c.png" /></p>
</div>


# Transmission and Reflection

These are linked to transmission and reflection via:


<div class="figure">
<p><img src="img/example_scattering_1d_3442db6737556748dbd7e9aa9a8b22066cfa1f67.png" alt="example_scattering_1d_3442db6737556748dbd7e9aa9a8b22066cfa1f67.png" /></p>
</div>

Choosing the global phase such that we can compare the phases at
<img src="img/example_scattering_1d_f3a850c6022001c89bdba8f4af42dfe892ed0dfe.png" alt="example_scattering_1d_f3a850c6022001c89bdba8f4af42dfe892ed0dfe.png" />, i.e. <img src="img/example_scattering_1d_1405f1ba730e2e407abc989e67bd0251c9231558.png" alt="example_scattering_1d_1405f1ba730e2e407abc989e67bd0251c9231558.png" />, we get
with


<div class="figure">
<p><img src="img/example_scattering_1d_4e149651dd0ab942cdd2e51b359c2df699e5f0d4.png" alt="example_scattering_1d_4e149651dd0ab942cdd2e51b359c2df699e5f0d4.png" /></p>
</div>

we have


<div class="figure">
<p><img src="img/example_scattering_1d_79d5584d1caf7ac0a35d6d2882cd8d7ba08121c2.png" alt="example_scattering_1d_79d5584d1caf7ac0a35d6d2882cd8d7ba08121c2.png" /></p>
</div>

which in the code below are called
`t * g = c + r * d`, i.e.,


<div class="figure">
<p><img src="img/example_scattering_1d_36f60021486769e58cdb9eac1db5b4824a980491.png" alt="example_scattering_1d_36f60021486769e58cdb9eac1db5b4824a980491.png" /></p>
</div>

and which we can write as a linear system of equations
for <img src="img/example_scattering_1d_e764246f405f6bbd04ab95dbdd287a2f66ab5615.png" alt="example_scattering_1d_e764246f405f6bbd04ab95dbdd287a2f66ab5615.png" /> and <img src="img/example_scattering_1d_6b2816ab2157d57ff3de6c581ae6ba86b3b2c989.png" alt="example_scattering_1d_6b2816ab2157d57ff3de6c581ae6ba86b3b2c989.png" />


<div class="figure">
<p><img src="img/example_scattering_1d_102f5648807b144b98af42891a1d095a8105878e.png" alt="example_scattering_1d_102f5648807b144b98af42891a1d095a8105878e.png" /></p>
</div>

and we can rewrite this as


<div class="figure">
<p><img src="img/example_scattering_1d_7227cff381505287ea3c604b6037a24d216fb3d3.png" alt="example_scattering_1d_7227cff381505287ea3c604b6037a24d216fb3d3.png" /></p>
</div>

and therefore


<div class="figure">
<p><img src="img/example_scattering_1d_762d245d121d26aee2b5d531c6b6993cab78a0ae.png" alt="example_scattering_1d_762d245d121d26aee2b5d531c6b6993cab78a0ae.png" /></p>
</div>


## Scattering Matrix

Note that we can more generally define:


<div class="figure">
<p><img src="img/example_scattering_1d_448ac7c59022504a1228f51740a0c89be08f0c5d.png" alt="example_scattering_1d_448ac7c59022504a1228f51740a0c89be08f0c5d.png" /></p>
</div>

where we this time explicitly differentiate between the <img src="img/example_scattering_1d_34e78eac9c17dd37c9c56b48e6b2375841a7fb4b.png" alt="example_scattering_1d_34e78eac9c17dd37c9c56b48e6b2375841a7fb4b.png" /> values
on both sides: <img src="img/example_scattering_1d_d26938a16d7a7fe0c6377a8e24c49226731a95cb.png" alt="example_scattering_1d_d26938a16d7a7fe0c6377a8e24c49226731a95cb.png" /> vs. <img src="img/example_scattering_1d_16cc34fcde7ddf0df4114d5967f977608c985928.png" alt="example_scattering_1d_16cc34fcde7ddf0df4114d5967f977608c985928.png" />. We use prefactors <img src="img/example_scattering_1d_ce257a5978dbbee7770e6f1dac1569e0754b1b41.png" alt="example_scattering_1d_ce257a5978dbbee7770e6f1dac1569e0754b1b41.png" /> for
incoming and <img src="img/example_scattering_1d_493f5ed61355ba46134454362bf4d446492bc7a7.png" alt="example_scattering_1d_493f5ed61355ba46134454362bf4d446492bc7a7.png" /> for outgoing components. Indices <img src="img/example_scattering_1d_08e52b1c89139291748d01c62586442e3f277a48.png" alt="example_scattering_1d_08e52b1c89139291748d01c62586442e3f277a48.png" /> correspond to
left (<img src="img/example_scattering_1d_3ca2ec59b4a81e6dc3d97e94e291bd5916fe90ef.png" alt="example_scattering_1d_3ca2ec59b4a81e6dc3d97e94e291bd5916fe90ef.png" />), indices <img src="img/example_scattering_1d_e869c67913d7f966007ed1a6a946946486a5124a.png" alt="example_scattering_1d_e869c67913d7f966007ed1a6a946946486a5124a.png" /> to right (<img src="img/example_scattering_1d_4bce61bcded1d90f108ebb9024d95e83bdc20ef8.png" alt="example_scattering_1d_4bce61bcded1d90f108ebb9024d95e83bdc20ef8.png" />).

With them the above becomes with
<img src="img/example_scattering_1d_6dfe724c95115c0eb012e9fbd0391b70d92051ca.png" alt="example_scattering_1d_6dfe724c95115c0eb012e9fbd0391b70d92051ca.png" />,
<img src="img/example_scattering_1d_afe26864229ce4cfef18d59efd7c028b16ddf7d3.png" alt="example_scattering_1d_afe26864229ce4cfef18d59efd7c028b16ddf7d3.png" />,
<img src="img/example_scattering_1d_46e1df1cb55748d15531ec2eee6b5bd3f3954580.png" alt="example_scattering_1d_46e1df1cb55748d15531ec2eee6b5bd3f3954580.png" />, and
<img src="img/example_scattering_1d_0dd639481baa66686ad46ac0bf51cad484a6aa9c.png" alt="example_scattering_1d_0dd639481baa66686ad46ac0bf51cad484a6aa9c.png" /> using


<div class="figure">
<p><img src="img/example_scattering_1d_8c48a96a3d51584ba8a8c49f04d7e35e77b15b31.png" alt="example_scattering_1d_8c48a96a3d51584ba8a8c49f04d7e35e77b15b31.png" /></p>
</div>

the following equation:


<div class="figure">
<p><img src="img/example_scattering_1d_edc2e9d90993077bd0bcd6f4586f577981ec58a9.png" alt="example_scattering_1d_edc2e9d90993077bd0bcd6f4586f577981ec58a9.png" /></p>
</div>

Such that we can map incoming to outgoing amplitudes


<div class="figure">
<p><img src="img/example_scattering_1d_50bf2ee01f9f2287a2f9da72d4e64adbcc119250.png" alt="example_scattering_1d_50bf2ee01f9f2287a2f9da72d4e64adbcc119250.png" /></p>
</div>

and therefore


<div class="figure">
<p><img src="img/example_scattering_1d_5879f8fc040aa036e8d57beba88c93f5c69aa3f5.png" alt="example_scattering_1d_5879f8fc040aa036e8d57beba88c93f5c69aa3f5.png" /></p>
</div>

hence


<div class="figure">
<p><img src="img/example_scattering_1d_c49aff0e8393151b717e4215b2c395d65fd03a71.png" alt="example_scattering_1d_c49aff0e8393151b717e4215b2c395d65fd03a71.png" /></p>
</div>


# See Also

<./example_scattering_1d.org>: org file with details

