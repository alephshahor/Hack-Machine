import sys
import os
from dff import DFF

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way1bit import Mux2Way1Bit

class Bit:

    def __init__(self):

        self.dff = DFF()

    def compute(self, _in, load):

        mux2Way1Bit = Mux2Way1Bit()
        dff_input = mux2Way1Bit.compute(load, self.dff.internal_state, _in)
        return self.dff.compute(dff_input)
