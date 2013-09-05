#/usr/bin/python -w

import platform
import numpy as np
import timeit
import fast_any_all as faa

#total 100 iterations, in batches of 10, taking the minimum as per: http://stackoverflow.com/a/8220943
iters=10
runs=10
datasize=5000000

setuptest='import numpy as np; import fast_any_all as faa; A = np.arange('+str(datasize)+'); B = np.arange('+str(datasize)+');'

# n.b. test case can't be abstracted out here, different representations for int maths or nested functions

# using np.any
test1='np.any([A>5, B<2,A>10], 0)'

# using integers in place of logic
test2='((A>5)+(B<2)+(A>10))>0'

# using nested logical_or operations
test3='np.logical_or(np.logical_or(A>5, B<2), A>10)'

# using faa any
test4='faa.any([A>5, B<2,A>10])'

# using reduce
test5='faa.reduce_any([(A>5),(B<2),(A>10)])'

# using boolean indexing
test6='faa.boolean_index_any([A>5, B<2,A>10])'

print "Benchmark of fast_any_all\n---\n\n"
print "System specification\n---\n\n"
print "Fast_any_all version: "+str(faa.__version__)+"\n"
print "Python version: "+platform.python_version()+"\n"
print "Numpy version: "+str(np.version.version)+"\n"

print "datasize="+str(datasize)+"\n"
print "iters="+str(iters)+"\n"

for i in [test1, test2, test3, test4, test5, test6] :
  print "\n`"+str(i)+"`\n---\n"
  exec(setuptest+"print "+i)
  print "\n"+str(min(timeit.repeat(stmt=i, setup=setuptest, number=iters, repeat=runs)))+"\n\n"

