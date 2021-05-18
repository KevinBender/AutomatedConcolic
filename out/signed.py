import z3, concolic

# This program is already instrumented. 
# If you remove all the lines with reference to `concolic`, you will see the original program
def signed(x):

  condition = concolic.get('x') < 0
  if (x < 0):
      concolic.guard(condition)
      y = -x
      concolic.set('y', -concolic.get('x'))
  else:
      concolic.guard(z3.Not(condition))
      y = x
      concolic.set('y', concolic.get('x'))

  # y must be nonnegative
  assert y >= 0
  concolic.guard(concolic.get('y') >= 0)

  # concolic: you can print your constraint in short-hand or SMT-LIB format:
  # concolic.dump_path()
  # concolic.dump_smt()

  return y

