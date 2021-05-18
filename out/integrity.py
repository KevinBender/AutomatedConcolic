from signed import signed
from f1 import f1
from f2 import f2
from sum import sum

assert signed(-1) == 1
assert signed(0) == 0
assert signed(1) == 1
assert signed(42) == 42

assert f1(0, 0) == 100
assert f1(10, 20) == 230
assert f1(-1, 0) == 1
try:
	raised = False
	f1(1, 1)
except AssertionError:
	raised = True
	pass
finally:
	assert raised, "Should have raised"

assert f2(0, 0, 0) == 2
assert f2(1, 0, 0) == 0
try:
	raised = False
	f2(0, 0, 1)
except AssertionError:
	raised = True
	pass
finally:
	assert raised, "Should have raised"

assert sum(0) == 0
assert sum(1) == 1
assert sum(2) == 3
assert sum(3) == 6
assert sum(4) == 10
assert sum(5) == 15
assert sum(6) == 0