import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from register16bit import Register16Bit

test_input = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
test_load = [1, 0, 1, 1]
test_output = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

register16Bit = Register16Bit()

def test_register16bit():
    for i in range(len(test_input)):
        result = register16Bit.compute(test_input[i], test_load[i])
        assert result == test_output[i], 'Error, in: {}, load: {} should output: {} but got: {}'.format(test_input[i - 1],
                                                                                                        test_load[i - 1],
                                                                                                        test_output[i],
                                                                                                        result)