import z3, concolic
# Instructors have filled out two lines of instrumentation; your job is to add more
def f1(x, z):
  if (x >= 0 and z <= 0):
      y = 100
  else:
      if (x >= 0 and z > x):
          t = x * z
          y = t + 30
      else:
          y = -x

  # y must be nonnegative
  assert y >= 0

 # you can print your constraint in short-hand or SMT-LIB format:
 # concolic.dump_path()
 # concolic.dump_smt()
  return y

