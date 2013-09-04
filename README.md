fast_any_all
----

Basically a ~14-17x faster implementation of a common use case for numpy.any() using numpy.logical_or().

Implementation is trivial. 

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


Please see BENCHMARK.md for example use.

To run benchmarks: python test_fast_any_all.py 


Todo
---

It's possible to make this implement more of the functionality of np.any by using reshape to alter which axis is used.

But for now, it's fast and has a nicer syntax than np.any() or np.logical_or() with my own use case, which is what I care about.

Licenses
--

GPL, MIT.


Thanks & copyleft
---

Norsk Institutt for Skog og Landskap
