import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from xor2way1bit import Xor2Way1Bit

a = [0, 0, 1, 1]
b = [0, 1, 0, 1]

output = [0, 1, 1, 0]

xor2Way1Bit = Xor2Way1Bit()


def test_xor2way1bit():
    for i in range(len(a)):
        result = xor2Way1Bit.compute(a[i], b[i])
        assert result == output[i], 'Error, a: {}, b: {}  should output: {} but got: {}'.format(a[i],
                                                                                                b[i],
                                                                                                output[i],
                                                                                                result)
