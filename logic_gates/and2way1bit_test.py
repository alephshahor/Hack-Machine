import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from and2way1bit import And2Way1Bit

n_inputs = 4

test_a = [0, 0, 1, 1]
test_b = [0, 1, 0, 1]
test_output = [0, 0, 0, 1]

and2Way1Bit = And2Way1Bit()


def test_and2way1bit():
    for i in range(n_inputs):
        result = and2Way1Bit.compute(test_a[i], test_b[i])
        assert result == test_output[i], 'Error, a[{}], b[{}] should output [{}] but got: [{}]'.format(test_a[i],
                                                                                                       test_b[i],
                                                                                                       test_output[i],
                                                                                                       result)
