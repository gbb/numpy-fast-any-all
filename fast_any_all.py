import numpy as np

# Purpose: 
# np.any and np.all are quite slow - about 10-20x slower than using logical_or and logical_and calls
# This code tries to combine the best features of np.logical_and/or and np.any/all. 
# It takes lists of arrays (like np.any/all), but is fast like np.logical_or/and
# It doesn't have the flexibility (in terms of axis choice) that is offered by np.any/all. 
# Benchmarking suggested there would be no performance advantage to using inplace np.logical_or/and.

def all(inputs):
  return fast_logic(inputs,np.logical_and)

def any(inputs):
  return fast_logic(inputs,np.logical_or)

def fast_logic(inputs, logic_func): 
  # No type-checking; use logical_or/and to check if the arrays are of the correct type (boolean or subtype)

  # Check if it's size 1
  if len(inputs)==1: 
    return inputs

  output = inputs[0] # separate out first element

  for w in range(1,len(inputs)):   # logical combination with other elements
    output=logic_func(output,inputs[w])
  
  return output
