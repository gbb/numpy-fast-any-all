fast_any_all
----

Basically a ~14-17x faster implementation of a common use case for numpy.any() using numpy.logical_or().

Implementation is trivial. 

Author
---

Graeme B. Bell

Usage
---

import fast_any_all as faa

faa.any([2d boolean array]), returns true where at least one element is true in axis 0

faa.all([2d boolean array]), return true where all elements are true in axis 0


Examples
---

Please see BENCHMARK.md for example use.

To run benchmarks: python test_fast_any_all.py 


Todo
---

It's possible to make this implement more of the functionality of np.any by using reshape to alter which axis is used.

But for now, it's super fast and syntactically nice for my own use case, which is what I care about.

Licenses
--

GPL, MIT.


Thanks & copyleft
---

Norsk Institutt for Skog og Landskap
