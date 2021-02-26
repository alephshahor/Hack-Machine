import pytest
from hack_machine.logic_gates.mux2way1bit import Mux2Way1Bit

test_input = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
test_output = [0, 0, 1, 1, 0, 1, 0, 1]

mux2Way1Bit = Mux2Way1Bit()


def test_mux2way1bit():
    for i in range(len(test_input)):
        result = mux2Way1Bit.compute(test_input[i][0], test_input[i][1], test_input[i][2])
        assert result == test_output[i], 'Error, sel[{}], a[{}], b[{}] should output: [{}] but got: [{}]'.format(
            test_input[i][0],
            test_input[i][1],
            test_input[i][2],
            test_output[i],
            result)
