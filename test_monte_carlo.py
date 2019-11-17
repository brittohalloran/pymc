import pytest
import monte_carlo as mc


def test_Norm():

    # Works normally
    a = mc.Norm(interval=(-1.645, 1.645))
    assert a.mean == 0
    assert abs(a.sd - 1) < 0.005

    # Bad combination of inputs
    with pytest.raises(Exception):
        a = mc.Norm(mean=0, interval=(0, 1))

    # Bad combination of inputs
    with pytest.raises(Exception):
        a = mc.Norm(mean=0, sd=1, interval=(0, 1))

    # Three number interval
    with pytest.raises(Exception):
        a = mc.Norm(interval=(0, 1, 2))

    # One number interval
    with pytest.raises(Exception):
        a = mc.Norm(interval=(0))


def test_sum_tuple():
    assert sum((1, 2, 3)) == 6

