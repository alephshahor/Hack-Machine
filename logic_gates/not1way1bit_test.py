import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from not1way1bit import Not1Way1Bit

test_input = [0, 1]
test_output = [1, 0]

not1Way1Bit = Not1Way1Bit()

def test_not1way1bit():
    for i in range(len(test_input)):
        result = not1Way1Bit.compute(test_input[i])
        assert result == test_output[i], 'Error, in: {} should output: {} but got: {}'.format(test_input[i], test_output[i], result)
