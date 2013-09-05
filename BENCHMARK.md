Benchmark of fast_any_all
---


System specification
---


Fast_any_all version: 1.0.0

Python version: 2.7.3

Numpy version: 1.7.1

datasize=5000000

iters=10


`np.any([A>5, B<2,A>10], 0)`
---

[ True  True False ...,  True  True  True]

2.90197491646



`((A>5)+(B<2)+(A>10))>0`
---

[ True  True False ...,  True  True  True]

0.267004966736



`np.logical_or(np.logical_or(A>5, B<2), A>10)`
---

[ True  True False ...,  True  True  True]

0.201917171478



`faa.any([A>5, B<2,A>10])`
---

[ True  True False ...,  True  True  True]

0.202533006668



`faa.reduce_any([(A>5),(B<2),(A>10)])`
---

[ True  True False ...,  True  True  True]

0.241019010544



`faa.boolean_index_any([A>5, B<2,A>10])`
---

[ True  True False ...,  True  True  True]

0.239975214005


