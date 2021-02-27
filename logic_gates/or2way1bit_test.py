import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from or2way1bit import Or2Way1Bit

test_a = [0, 0, 1, 1]
test_b = [0, 1, 0, 1]
test_output = [0, 1, 1, 1]

or2way1bit = Or2Way1Bit()

def test_or2way1bit():
    for i in range(len(test_a)):
        result = or2way1bit.compute(test_a[i], test_b[i])
        assert result == test_output[i], 'Error, a: {},  b: {} should output: {} but got: {}'.format(test_a[i],
                                                                                                     test_b[i],
                                                                                                     test_output[i],
                                                                                                     result)
