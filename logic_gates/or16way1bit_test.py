import pytest

from or16way1bit import Or16Way1Bit

or16Way1Bit = Or16Way1Bit()


def test_or16way1bit():

    _in = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert or16Way1Bit.compute(_in) == 0

    _in = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert or16Way1Bit.compute(_in) == 1
