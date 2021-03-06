import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from dmux4way1bit import DMux4Way1Bit

test_input = [1, 1, 1, 1]
test_sel = [[0, 0], [0, 1], [1, 0], [1, 1]]
test_output = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

dMux4Way1Bit = DMux4Way1Bit()


def test_dmux4way1bit():
    for i in range(len(test_input)):
        result = dMux4Way1Bit.compute(test_sel[i], test_input[i])
        assert result == test_output[i], 'Error, sel{}, in{} should output: {} but got: {}'.format(test_sel[i],
                                                                                                   test_input[i],
                                                                                                   test_output[i],
                                                                                                   result)
