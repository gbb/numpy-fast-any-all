import numpy as np

# Purpose: 
# np.any and np.all are quite slow - about 15x slower than using logical_or and logical_and calls
# This code tries to combine the best features of np.logical_and/or and np.any/all. 
# It takes lists of arrays (like np.any/all), but is fast like np.logical_or/and
# It doesn't have the flexibility (in terms of axis choice) that is offered by np.any/all. 


def all(inputs):
  """faa.all([list of boolean ndarrays]), returns true where at least one element is true in an ndarray at that position.
  """
  return fast_logic(inputs,np.logical_and)


def any(inputs):
  """faa.any([list of boolean ndarrays]), returns true where at least one element is true in an ndarray at that position.
  """
  return fast_logic(inputs,np.logical_or)


def fast_logic(inputs, logic_func): 
  """ generic helper function for any() and all()
      No direct type-checking; relies on numpy.boolean_or/and. 
  "" 

  # Catch empty input, retain compatibility with np.any return value. 
  if len(inputs)==0: 
    return False

  output = inputs[0] # separate out first element

  for w in range(1,len(inputs)):   # logical combination with other elements
    output=logic_func(output,inputs[w])   # note that this loop doesn't run when len(inputs)=1.
  
  return output
