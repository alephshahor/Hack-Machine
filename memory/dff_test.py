import pytest
import sys
import os


sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from dff import DFF


test_input = [0, 1, 0, 1]
test_output = [0, 0, 1, 0]

dff = DFF()

def test_dff():
    for i in range(len(test_input)):
        result = dff.compute(test_input[i])
        assert result == test_output[i], 'Error, in: {}, should output: {} but got: {}'.format(test_input[i - 1],
                                                                                               test_output[i],
                                                                                               result)
