from . import utils


def test_first():
    assert utils.fibonacci(1) == 1


def test_fifth():
    assert utils.fibonacci(5) == 5


def test_seventh():
    assert utils.fibonacci(7) == 13