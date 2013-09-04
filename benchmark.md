Benchmark
---


datasize=500000
iters=10


np.any([A>5, B<2,A>10], 0)
[ True  True False ...,  True  True  True]
0.398867845535


((A>5)+(B<2)+(A>10))>0
[ True  True False ...,  True  True  True]
0.0300221443176


np.logical_or(np.logical_or(A>5, B<2), A>10)
[ True  True False ...,  True  True  True]
0.0227630138397


faa.any([(A>5),(B<2),(A>10)])
[ True  True False ...,  True  True  True]
0.0228819847107

