import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from or2way1bit import Or2Way1Bit

class Or8Way1Bit:

    def compute(self, _in):

        assert len(_in) == 8

        or2Way1Bit = Or2Way1Bit()

        result = _in[0]
        for i in range(len(_in)-1):
            result = or2Way1Bit.compute(result, _in[i+1])

        return result
