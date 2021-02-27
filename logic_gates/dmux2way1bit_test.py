import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from dmux2way1bit import DMux2Way1Bit

test_input = [1, 1]
test_sel = [0, 1]
test_output = [[1, 0], [0, 1]]

dMux2Way1Bit = DMux2Way1Bit()


def test_dmux2way1bit():
    for i in range(len(test_input)):
        result = dMux2Way1Bit.compute(test_sel[i], test_input[i])
        assert result == test_output[i], 'Error, sel[{}], in[{}] should output: {} but got: {}'.format(test_sel[i],
                                                                                                       test_input[i],
                                                                                                       test_output[i],
                                                                                                       result)
