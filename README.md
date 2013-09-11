fast_any_all
----

Basically a 30x faster implementation of a common use case for numpy.any/all() using numpy.logical_or/and(). Implementation is trivial. 

It might be helpful to think of this as an extended version of logical_or/and.

It was written to improve performance in situations where you are overlaying identically shaped arrays and building boolean masks within the shaped array. 

For example, if you have 3 raster images, A, B and C, representing different aspects of some data, and in the same shape: 

For each pixel location: 
  if A[location] has the value 3,5, or 7, and B[location] has a value <100, and C[location] has a value 8, then output[location]=True

This can be conveniently represented in terms of any() and all():   `all(any([A==3, A==5, A==7]), B<100, C==8)`

The resulting masks can be combined with [simpleselect](https://github.com/gbb/numpy-simple-select) to enable fast, complex raster-based decisions. This is rather useful for GIS work. 

Please note that in the experimental numpy1.8 branch, numpy.any/all are much improved over 1.7, but are expected to be around 40-50% slower than fast_any_all.

Performance has been tested with a range of alternative implementations and idiomatic approaches.

Author
---

Graeme B. Bell

Usage
---

`import fast_any_all as faa`

`faa.any([list of boolean ndarrays])`, returns true where at least one element is true in an ndarray at that position.

`faa.all([list of boolean ndarrays])`, returns true where at least one element is true in an ndarray at that position.


Examples
---

`import fast_any_all as faa`

`import numpy as np`

`A = np.arange(5000)`

`print faa.any([A<1, A>5])`


Please see [BENCHMARK.md](BENCHMARK.md) for example use.

To run benchmarks: python test_fast_any_all.py 


Todo
---

It's possible to make this implement more of the functionality of np.any by using reshape to alter which axis is used.

But for now, it's fast and has a nicer syntax than np.any() or np.logical_or() with my own use case, which is what I care about.

Licenses
--

GPL, MIT.


Notes
---

I have also tried:

1. Using boolean addressing to overlay repeatedly. 15-20% slower than logical_or

2. Using the ,out facility of logical_or. Appeared to have no effect on performance.

3. vstack and other idioms (via Julian Taylor)

Thanks & copyleft
---

Norsk Institutt for Skog og Landskap
