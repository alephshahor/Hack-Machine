import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way1bit import Mux2Way1Bit

class Mux4Way1Bit:

    def compute(self, sel, a, b, c, d):

        assert len(sel) == 2

        mux2Way1Bit_1 = Mux2Way1Bit()
        mux2Way1Bit_1_out = mux2Way1Bit_1.compute(sel[1], a, b)

        mux2Way1Bit_2 = Mux2Way1Bit()
        mux2Way1Bit_2_out = mux2Way1Bit_2.compute(sel[1], c, d)

        mux2Way1Bit_3 = Mux2Way1Bit()
        mux2Way1Bit_3_out = mux2Way1Bit_3.compute(sel[0], mux2Way1Bit_1_out, mux2Way1Bit_2_out)

        return mux2Way1Bit_3_out



