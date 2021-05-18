import z3, concolic


def f2(a, b, c):
    x = 0
    concolic.set('x', 0)
    y = 0
    concolic.set('y', 0)
    z = 0
    concolic.set('z', 0)
    if a != 0:
        concolic.guard(concolic.get('a') != 0)
        x = -2
        concolic.set('x', -2)
    else:
        concolic.guard(z3.Not(concolic.get('a') != 0))
    if b < 5:
        concolic.guard(concolic.get('b') < 5)
        if a == 0 and c != 0:
            concolic.guard(z3.And(concolic.get('a') == 0, concolic.get('c') !=
                0))
            y = 1
            concolic.set('y', 1)
        else:
            concolic.guard(z3.Not(z3.And(concolic.get('a') == 0, concolic.
                get('c') != 0)))
        z = 2
        concolic.set('z', 2)
    else:
        concolic.guard(z3.Not(concolic.get('b') < 5))
    assert x + y + z != 3
    concolic.guard(concolic.get('x') + concolic.get('y') + concolic.get('z'
        ) != 3)
    return x + y + z
