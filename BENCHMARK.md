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

2.88760590553



`((A>5)+(B<2)+(A>10))>0`
---

[ True  True False ...,  True  True  True]

0.26745891571



`np.logical_or(np.logical_or(A>5, B<2), A>10)`
---

[ True  True False ...,  True  True  True]

0.199987888336



`faa.any_without_vstack([A>5, B<2,A>10])`
---

[ True  True False ...,  True  True  True]

0.203147172928



`faa.reduce_any([(A>5),(B<2),(A>10)])`
---

[ True  True False ...,  True  True  True]

0.243079185486



`faa.boolean_index_any([A>5, B<2,A>10])`
---

[ True  True False ...,  True  True  True]

0.237656116486



`np.any(b, 0)`
---

[ True  True False ...,  True  True  True]

0.244158983231



`np.any(np.vstack(a),0)`
---

[ True  True False ...,  True  True  True]

0.138797998428



`faa.any(a)`
---

[ True  True False ...,  True  True  True]

0.0958449840546


