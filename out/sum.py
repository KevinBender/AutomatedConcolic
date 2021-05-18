import z3, concolic


def sum(x):
    i = 0
    concolic.set('i', 0)
    r = 0
    concolic.set('r', 0)
    if x > 0 and x <= 5:
        concolic.guard(z3.And(concolic.get('x') > 0, concolic.get('x') <= 5))
        while i < x:
            concolic.guard(concolic.get('i') < concolic.get('x'))
            i = i + 1
            concolic.set('i', concolic.get('i') + 1)
            r = r + i
            concolic.set('r', concolic.get('r') + concolic.get('i'))
        else:
            concolic.guard(z3.Not(concolic.get('i') < concolic.get('x')))
        assert r == x * (x + 1) / 2
        concolic.guard(concolic.get('r') == concolic.get('x') * (concolic.
            get('x') + 1) / 2)
    else:
        concolic.guard(z3.Not(z3.And(concolic.get('x') > 0, concolic.get(
            'x') <= 5)))
    return r
