import pytest
import sys
from half_adder import HalfAdder

test_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
test_output = [[0, 0], [1, 0], [1, 0], [0, 1]]

half_adder = HalfAdder()

def test_half_adder():
    for i in range(len(test_input)):
        a = test_input[i][0]
        b = test_input[i][1]

        sum, carry = half_adder.compute(a, b)

        assert sum == test_output[i][0] or carry == test_output[i][1], 'Error, a: {}, b: {} should output {},'\
                                                                       '{} but got: {}, {}'.format(a,
                                                                                                   b,
                                                                                                   test_output[i][0],
                                                                                                   test_output[i][1],
                                                                                                   sum,
                                                                                                   carry)

