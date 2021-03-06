#/usr/bin/python -w

import platform
import numpy as np
import timeit
import fast_any_all as faa

#total 100 iterations, in batches of 10, taking the minimum as per: http://stackoverflow.com/a/8220943
iters=10
runs=10
datasize=5000000

setuptest='import numpy as np; import fast_any_all as faa; A = np.arange('+str(datasize)+'); B = np.arange('+str(datasize)+'); a = [[A>5,B<2,A>10] for i in range(1,10)]; b = np.empty([3] + list(A.shape)); b[0] = A>5; b[1] = B<2; b[2] = A>10;'

# n.b. test case can't be abstracted out here, different representations for int maths or nested functions

# using np.any
test1='np.any(a[0], 0)'

# using integers in place of logic
test2='((A>5)+(B<2)+(A>10))>0'

# using nested logical_or operations
test3='np.logical_or(np.logical_or(A>5, B<2), A>10)'

# using faa any
test4='faa.any(a[1])'

# using reduce
test5='faa.reduce_any(a[2])'

# using boolean indexing
test6='faa.boolean_index_any(a[3])'

# using np.any() with the 'list' idiom (Julian Taylor)
test7='np.any(b, 0)'

# using np.any() with the 'vstack' idiom (Julian Taylor)
test8='np.any(np.vstack(a[4]),0)'

# using faa.any() with the 'vstack' idiom (out of curiosity...)
test9='faa.any(np.vstack(a[5]))'


print "Benchmark of fast_any_all\n---\n\n"
print "System specification\n---\n\n"
print "Fast_any_all version: "+str(faa.__version__)+"\n"
print "Python version: "+platform.python_version()+"\n"
print "Numpy version: "+str(np.version.version)+"\n"

print "datasize="+str(datasize)+"\n"
print "iters="+str(iters)+"\n"

exec(setuptest)

for i in [test1, test2, test3, test4, test5, test6, test7, test8, test9] :
  print "\n`"+str(i)+"`\n---\n"
  exec("print "+i)
  print "\n"+str(min(timeit.repeat(stmt=i, setup=setuptest, number=iters, repeat=runs)))+"\n\n"

