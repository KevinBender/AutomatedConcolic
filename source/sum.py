import z3, concolic

# Computes sum of numbers from 1 to x if 1 <= x <= 5
def sum(x):
    i = 0
    r = 0
    if x > 0 and x <= 5:
        while i < x:
            i = i + 1
            r = r + i
        assert r == (x * (x+1)) / 2
    return r
