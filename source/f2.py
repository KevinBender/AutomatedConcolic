import z3, concolic

# Sample from lecture on symbolic execution
def f2(a, b, c):
    x = 0
    y = 0
    z = 0

    if (a != 0):
        x = -2
    if (b < 5):
        if (a == 0 and c != 0):
            y = 1
        z = 2
    assert(x + y + z != 3)
    return x + y + z
