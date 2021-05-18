import z3, concolic
# Instructors have filled out two lines of instrumentation; your job is to add more
def f1(x, z):
  b1 = z3.And(concolic.get('x') >= 0, concolic.get('z') <= 0)
  if (x >= 0 and z <= 0):
      concolic.guard(b1)
      y = 100
      concolic.set('y', 100)
  else:
      concolic.guard(z3.Not(b1))
      b2 = z3.And(concolic.get('x') >= 0, concolic.get('z') > concolic.get('x'))
      if (x >= 0 and z > x):
          concolic.guard(b2)
          t = x * z
          concolic.set('t', concolic.get('x') * concolic.get('z'))
          y = t + 30
          concolic.set('y', concolic.get('t'))
      else:
          concolic.guard(z3.Not(b2))
          y = -x
          concolic.set('y', -concolic.get('x'))

  # y must be nonnegative
  assert y >= 0
  concolic.guard(True) # Filled out by instructors

 # you can print your constraint in short-hand or SMT-LIB format:
 # concolic.dump_path()
 # concolic.dump_smt()
  return y

