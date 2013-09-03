#/usr/bin/python -w

import numpy as np
import timeit
import fast_any_all as fastaa

#total 100 iterations, in batches of 10, taking the minimum as per: http://stackoverflow.com/a/8220943
iters=10
runs=10
datasize=5000000

setuptest='import numpy as np; import fast_any_all as fastaa; A = np.arange('+str(datasize)+'); B = np.arange('+str(datasize)+');'

# using np.any
test1='np.any([A>5, B<2,A>10], 0)'

# using integers in place of logic
test2='((A>5)+(B<2)+(A>10))>0'

# using nested logical_or operations
test3='np.logical_or(np.logical_or(A>5, B<2), A>10)'

# using fastaa any
test4='fastaa.any([(A>5),(B<2),(A>10)])'

for i in [test1, test2, test3, test4] :
  print i
  exec(setuptest+"print "+i)
  print min(timeit.repeat(stmt=i, setup=setuptest, number=iters, repeat=runs))

