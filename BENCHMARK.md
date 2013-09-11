Benchmark of fast_any_all
---


System specification
---


Fast_any_all version: 1.0.0

Python version: 2.7.3

Numpy version: 1.7.1

datasize=5000000

iters=10


`np.any(a[0], 0)`
---

[ True  True False ...,  True  True  True]

2.67618393898



`((A>5)+(B<2)+(A>10))>0`
---

[ True  True False ...,  True  True  True]

0.267272949219



`np.logical_or(np.logical_or(A>5, B<2), A>10)`
---

[ True  True False ...,  True  True  True]

0.20156788826



`faa.any(a[1])`
---

[ True  True False ...,  True  True  True]

0.0790700912476



`faa.reduce_any(a[2])`
---

[ True  True False ...,  True  True  True]

0.118819952011



`faa.boolean_index_any(a[3])`
---

[ True  True False ...,  True  True  True]

0.115568161011



`np.any(b, 0)`
---

[ True  True False ...,  True  True  True]

0.244898796082



`np.any(np.vstack(a[4]),0)`
---

[ True  True False ...,  True  True  True]

0.141221046448



`faa.any(np.vstack(a[5]))`
---

[ True  True False ...,  True  True  True]

0.0991821289062


