fast_any_all
----

Basically a 15x faster implementation of a common use case for numpy.any() using numpy.logical_or().
Implementation is trivial. 


Usage
---

import fast_any_all as faa
faa.any([2d boolean array]), returns true where at least one element is true in axis 0
faa.all([2d boolean array]), return true where all elements are true in axis 0


Examples
---

See BENCHMARK.md


Todo
---

I think it's possible to make this implement more of the functionality of np.any by using reshape to alter which axis is used.
Not sure. It's super fast and syntactically nice for my own use case, which is what I care about.
