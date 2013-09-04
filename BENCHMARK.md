Benchmark
---


datasize=5000000
iters=10


`np.any([A>5, B<2,A>10], 0)`
---

[ True  True False ...,  True  True  True]

4.09605789185


`((A>5)+(B<2)+(A>10))>0`
---

[ True  True False ...,  True  True  True]

0.377617120743



`np.logical_or(np.logical_or(A>5, B<2), A>10)`
---

[ True  True False ...,  True  True  True]

0.287179946899



`faa.any([(A>5),(B<2),(A>10)])`
---

[ True  True False ...,  True  True  True]

0.285892963409


