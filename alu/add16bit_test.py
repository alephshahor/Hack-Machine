import pytest
import sys
from add16bit import Add16Bit

test_a_input = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0]]
test_b_input = [[0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]]
test_output = [[1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]]

add16Bit = Add16Bit()


def test_add16bit():

    for i in range(len(test_a_input)):

        a = test_a_input[i]
        b = test_b_input[i]

        result = add16Bit.compute(a, b)

        assert result == test_output[i], 'Error, a: {}, b: {} should output {} but got: {}.'.format(a, b, test_output[i], result)