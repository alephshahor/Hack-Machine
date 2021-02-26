import pytest
from hack_machine.logic_gates.or2way16bit import Or2Way16Bit

a = [[0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]

b = [[0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

output = [[0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

or2Way16Bit = Or2Way16Bit()

def test_or2way16bit():
    for i in range(len(a)):
        result = or2Way16Bit.compute(a[i], b[i])
        assert result == output[i], 'Error, a: {}, b: {} should output: {} but got: {}'.format(a[i],
                                                                                                   b[i],
                                                                                                   output[i],
                                                                                                   result)
