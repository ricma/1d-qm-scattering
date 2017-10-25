

# Example

Based on the script <./example_scattering_1d.py>

![img](./figures/example_scattering_1d.svg)


# Discretization

We use <img src="img/example_scattering_1d_7df349046e4e82a2fb8f43357b647c72164d4522.png" alt="example_scattering_1d_7df349046e4e82a2fb8f43357b647c72164d4522.png" />
and define <img src="img/example_scattering_1d_420dccf88e36c30418dab25834f1fc79833fbf5d.png" alt="example_scattering_1d_420dccf88e36c30418dab25834f1fc79833fbf5d.png" />
such that the Hamiltonian reads


<div class="figure">
<p><img src="img/example_scattering_1d_3ca971af33de0165e3787e0146ba1d9f3be5f850.png" alt="example_scattering_1d_3ca971af33de0165e3787e0146ba1d9f3be5f850.png" /></p>
</div>

and therefore:


<div class="figure">
<p><img src="img/example_scattering_1d_a3635db04e6875a89125169760eb3466b26635de.png" alt="example_scattering_1d_a3635db04e6875a89125169760eb3466b26635de.png" /></p>
</div>


# Transfer Matrix

This allows to write a transfer matrix <img src="img/example_scattering_1d_1dc03ff51b7c845d4b25362b4110feae0ea072cb.png" alt="example_scattering_1d_1dc03ff51b7c845d4b25362b4110feae0ea072cb.png" /> from
<img src="img/example_scattering_1d_f70aebeb6be64232f02b7d9fecc7db75e35bba7c.png" alt="example_scattering_1d_f70aebeb6be64232f02b7d9fecc7db75e35bba7c.png" />
as


<div class="figure">
<p><img src="img/example_scattering_1d_e72fd6f57bb71de29741a2c8b4af976795b2608a.png" alt="example_scattering_1d_e72fd6f57bb71de29741a2c8b4af976795b2608a.png" /></p>
</div>

and


<div class="figure">
<p><img src="img/example_scattering_1d_9e58f255d2c55a66da55a204d9d519e5d7492b00.png" alt="example_scattering_1d_9e58f255d2c55a66da55a204d9d519e5d7492b00.png" /></p>
</div>

connecting the first two and the last two elements of <img src="img/example_scattering_1d_fd32f1af1a573a885a771662179da7141316e5a6.png" alt="example_scattering_1d_fd32f1af1a573a885a771662179da7141316e5a6.png" />:


<div class="figure">
<p><img src="img/example_scattering_1d_d084ff64b4797ee2798e2342f87cffe400f5a986.png" alt="example_scattering_1d_d084ff64b4797ee2798e2342f87cffe400f5a986.png" /></p>
</div>


# Transmission and Reflection

These are linked to transmission and reflection via:


<div class="figure">
<p><img src="img/example_scattering_1d_b5e350962e71f853963e81eb14f01e04ebc753d3.png" alt="example_scattering_1d_b5e350962e71f853963e81eb14f01e04ebc753d3.png" /></p>
</div>

Choosing the global phase such that we can compare the phases at
<img src="img/example_scattering_1d_a3be07e0966961477853005c9f1b5f5fcf8272a5.png" alt="example_scattering_1d_a3be07e0966961477853005c9f1b5f5fcf8272a5.png" />, i.e. <img src="img/example_scattering_1d_f0c841dc0343badfae90829e9faf17b4732dac0e.png" alt="example_scattering_1d_f0c841dc0343badfae90829e9faf17b4732dac0e.png" />, we get
with


<div class="figure">
<p><img src="img/example_scattering_1d_068bc7db81658e9eb4f80cfeb0b6179c54487b28.png" alt="example_scattering_1d_068bc7db81658e9eb4f80cfeb0b6179c54487b28.png" /></p>
</div>

we have


<div class="figure">
<p><img src="img/example_scattering_1d_db3155adb2e9dcbb3c5c82b96218ace016065f58.png" alt="example_scattering_1d_db3155adb2e9dcbb3c5c82b96218ace016065f58.png" /></p>
</div>

which in the code below are called
`t * g = c + r * d`, i.e.,


<div class="figure">
<p><img src="img/example_scattering_1d_271a542df3051678184f0d4c098a2309f7abbf7f.png" alt="example_scattering_1d_271a542df3051678184f0d4c098a2309f7abbf7f.png" /></p>
</div>

and which we can write as a linear system of equations
for <img src="img/example_scattering_1d_0759ad1928017b8a5f099c51a8d68b36f9b1c8c6.png" alt="example_scattering_1d_0759ad1928017b8a5f099c51a8d68b36f9b1c8c6.png" /> and <img src="img/example_scattering_1d_fc023ccaec24b3df4514a72f47328965ece58155.png" alt="example_scattering_1d_fc023ccaec24b3df4514a72f47328965ece58155.png" />


<div class="figure">
<p><img src="img/example_scattering_1d_406bd34595901d3c6d050e12b623a2fb51948707.png" alt="example_scattering_1d_406bd34595901d3c6d050e12b623a2fb51948707.png" /></p>
</div>

and we can rewrite this as


<div class="figure">
<p><img src="img/example_scattering_1d_bcd2583487cd6df1d7724f8fb935e78db3959b84.png" alt="example_scattering_1d_bcd2583487cd6df1d7724f8fb935e78db3959b84.png" /></p>
</div>

and therefore


<div class="figure">
<p><img src="img/example_scattering_1d_2f472088c983412f19dcbbf6da689f4fde7e78bf.png" alt="example_scattering_1d_2f472088c983412f19dcbbf6da689f4fde7e78bf.png" /></p>
</div>


## Scattering Matrix

Note that we can more generally define:


<div class="figure">
<p><img src="img/example_scattering_1d_cac9c139b73b64d2f5c277d9a43959fdfa049999.png" alt="example_scattering_1d_cac9c139b73b64d2f5c277d9a43959fdfa049999.png" /></p>
</div>

where we this time explicitly differentiate between the <img src="img/example_scattering_1d_f53f1b6927585e37a208a679c9686852c3c32cca.png" alt="example_scattering_1d_f53f1b6927585e37a208a679c9686852c3c32cca.png" /> values
on both sides: <img src="img/example_scattering_1d_7720f4396d1ce265c770215c36e8d25a1e3949ee.png" alt="example_scattering_1d_7720f4396d1ce265c770215c36e8d25a1e3949ee.png" /> vs. <img src="img/example_scattering_1d_2699fe73ebe2e56fc0585ec6f3b2fc3646fd6f11.png" alt="example_scattering_1d_2699fe73ebe2e56fc0585ec6f3b2fc3646fd6f11.png" />. We use prefactors <img src="img/example_scattering_1d_a5bd3e935a345ffee2fac684d5d0c715d4e0dadb.png" alt="example_scattering_1d_a5bd3e935a345ffee2fac684d5d0c715d4e0dadb.png" /> for
incoming and <img src="img/example_scattering_1d_44529c86af0ce0386e7c0affe2e8c4741f67c224.png" alt="example_scattering_1d_44529c86af0ce0386e7c0affe2e8c4741f67c224.png" /> for outgoing components. Indices <img src="img/example_scattering_1d_c5b9d7883a1473685ff3259657d25ad9077fdd4b.png" alt="example_scattering_1d_c5b9d7883a1473685ff3259657d25ad9077fdd4b.png" /> correspond to
left (<img src="img/example_scattering_1d_165e9dfa2a79988f59e6804213c06d6e3554b5cc.png" alt="example_scattering_1d_165e9dfa2a79988f59e6804213c06d6e3554b5cc.png" />), indices <img src="img/example_scattering_1d_bac757945feafd03c7a75740245e8c94dea4fe4c.png" alt="example_scattering_1d_bac757945feafd03c7a75740245e8c94dea4fe4c.png" /> to right (<img src="img/example_scattering_1d_96a2a43e9dbd2c1301c9045ded5eb4c94a2ef363.png" alt="example_scattering_1d_96a2a43e9dbd2c1301c9045ded5eb4c94a2ef363.png" />).

With them the above becomes with
<img src="img/example_scattering_1d_c325695bb07dd7782e89a7f606a05981060d5c1d.png" alt="example_scattering_1d_c325695bb07dd7782e89a7f606a05981060d5c1d.png" />,
<img src="img/example_scattering_1d_1279cacb8b1bfb8cb59cf1099175ca4bd78a3cb2.png" alt="example_scattering_1d_1279cacb8b1bfb8cb59cf1099175ca4bd78a3cb2.png" />,
<img src="img/example_scattering_1d_e96cee3bc1cb6a3e8d0e9fdf6e087277011512bb.png" alt="example_scattering_1d_e96cee3bc1cb6a3e8d0e9fdf6e087277011512bb.png" />, and
<img src="img/example_scattering_1d_e938a43acd71bb5a8f10ec9f78674afef07d2923.png" alt="example_scattering_1d_e938a43acd71bb5a8f10ec9f78674afef07d2923.png" /> using


<div class="figure">
<p><img src="img/example_scattering_1d_c49fd062e89e0e877d635594a185edc11d7db007.png" alt="example_scattering_1d_c49fd062e89e0e877d635594a185edc11d7db007.png" /></p>
</div>

the following equation:


<div class="figure">
<p><img src="img/example_scattering_1d_17849e2f267eeed0d8aaeaa527ed2c07d094d11d.png" alt="example_scattering_1d_17849e2f267eeed0d8aaeaa527ed2c07d094d11d.png" /></p>
</div>

Such that we can map incoming to outgoing amplitudes


<div class="figure">
<p><img src="img/example_scattering_1d_5724859c8a560701b3fd1646e85816123d7b93c0.png" alt="example_scattering_1d_5724859c8a560701b3fd1646e85816123d7b93c0.png" /></p>
</div>

and therefore


<div class="figure">
<p><img src="img/example_scattering_1d_ea5695cdbf20f007f9196a6c5127c498d4e39dc4.png" alt="example_scattering_1d_ea5695cdbf20f007f9196a6c5127c498d4e39dc4.png" /></p>
</div>

hence


<div class="figure">
<p><img src="img/example_scattering_1d_be43f24f5ff6db754bf46d2ef4a43e3f4662daa8.png" alt="example_scattering_1d_be43f24f5ff6db754bf46d2ef4a43e3f4662daa8.png" /></p>
</div>


# See Also

<example_scattering_1d.md>: org file with details

[github repo](https://github.com/ricma/1d-qm-scattering)

