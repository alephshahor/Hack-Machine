import pytest

from bit import Bit

test_input = [1, 0, 0, 0, 0]
test_load = [1, 0, 0, 1, 0]
test_output = [0, 1, 1, 1, 0]

bit = Bit()

def test_bit():
    for i in range(len(test_input)):
        result = bit.compute(test_input[i], test_load[i])
        assert result == test_output[i],'Error, in: {}, load: {} should output: {} but got: {}'.format(test_input[i - 1],
                                                                                                           test_load[i - 1],
                                                                                                           test_output[i],
                                                                                                           result)

