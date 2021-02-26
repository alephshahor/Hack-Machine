import pytest
from hack_machine.logic_gates.mux2way1bit import Mux2Way1Bit

test_input = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

input_a = [0, 0, 1, 1, 0, 0, 1, 1]
input_b = [0, 1, 0, 1, 0, 1, 0, 1]
selector = [0, 0, 0, 0, 1, 1, 1, 1]
output = [0, 0, 1, 1, 0, 1, 0, 1]

n_iterations = len(input_a)
mux2Way1Bit = Mux2Way1Bit()


def test_mux2way1bit():
    for i in range(n_iterations):
        result = mux2Way1Bit.compute(selector[i], input_a[i], input_b[i])
        assert result == output[i], 'Error, sel[{}], a[{}], b[{}] should output: [{}] but got: [{}]'.format(
            selector[i],
            input_a[i],
            input_b[i],
            output[i],
            result)
