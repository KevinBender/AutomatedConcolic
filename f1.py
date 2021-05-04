import z3, concolic
# Instructors have filled out two lines of instrumentation; your job is to add more
def f1(x, z):
  if( x + 4 < 2 and z +2 > 3+2 or 2*3==5):
    print('i')
  if (x >= 0 and z <= 0):
      y = 100
  elif(x == 2):
      pp = 20
  else:
      pp = 5
  return y

