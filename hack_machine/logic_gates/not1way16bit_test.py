import sys
from hack_machine.logic_gates.not1way16bit import Not1Way16Bit

test_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

test_output = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]

not1Way16Bit = Not1Way16Bit()

def test_not1way16bit():
    for i in range(len(test_input)):
        assert not1Way16Bit.compute(test_input[i]) == test_output[i], 'Error, the input {} should'\
                                                                      ' output: {}'.format(test_input[i],
                                                                                           test_output[i])
