import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.Or(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.Or(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
import z3, concolic


def f1(x, z):
    if x >= 0 and z <= 0:
        concolic.guard(z3.And(concolic.get('x') >= 0, concolic.get('z') <= 0))
        y = 100
        concolic.set('y', 100)
    else:
        concolic.guard(z3.Not(z3.And(concolic.get('x') >= 0, concolic.get(
            'z') <= 0)))
        if x >= 0 and z > x:
            concolic.guard(z3.And(concolic.get('x') >= 0, concolic.get('z') >
                concolic.get('x')))
            t = x * z
            concolic.set('t', x * z)
            y = t + 30
            concolic.set('y', t + 30)
        else:
            concolic.guard(z3.Not(z3.And(concolic.get('x') >= 0, concolic.
                get('z') > concolic.get('x'))))
            y = -x
            concolic.set('y', -x)
    assert y >= 0
    concolic.guard(concolic.get('y') >= 0)
    return y
