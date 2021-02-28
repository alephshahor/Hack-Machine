import pytest
import sys
import os

from pc import Pc

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

pc = Pc()
zero = [0] * 16


def test_pc():
    _in = conversions.dec_to_bin_arr(16, 25)
    result = pc.compute(_in, inc=0, load=1, reset=0)
    assert result == zero, 'Error, expected {} but got {}'.format(zero, result)

    result = pc.compute(_in, inc=0, load=0, reset=0)
    assert result == _in, 'Error, expected {} but got {}'.format(_in, result)

    result = pc.compute(_in, inc=1, load=0, reset=0)
    assert result == _in, 'Error, expected {} but got {}'.format(_in, result)

    result = pc.compute(_in, inc=1, load=0, reset=1)
    assert result == conversions.dec_to_bin_arr(16, 26), 'Error, expected {} but got {}'.format(conversions.dec_to_bin_arr(16, 26), result)

    result = pc.compute(_in, inc=1, load=0, reset=0)
    assert result == zero, 'Error, expected {} but got {}'.format(zero, result)

    result = pc.compute(_in, inc=0, load=0, reset=0)
    assert result == zero[:15] + [1], 'Error, expected {} but got {}'.format((zero[:15] + 1), result)

