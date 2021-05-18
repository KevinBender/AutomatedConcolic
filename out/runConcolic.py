import concolic, sys
# Run concolic execution and compare expected result

def test_run(name, vars):
	print("\n\n\n####### Test %s #######\n" % name)
	func = getattr(__import__(name), name)
	paths, bug = concolic.run(func, vars)
    
    
name = sys.argv[1]
vars = sys.argv[2:]

test_run(name, vars)
