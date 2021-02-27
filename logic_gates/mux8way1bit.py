import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way1bit import Mux2Way1Bit
from mux4way1bit import Mux4Way1Bit

class Mux8Way1Bit:

    def compute(self, sel, a, b, c, d, e, f, g, h):

        assert len(sel) == 3

        # 0 1 1
        mux4way1bit_1 = Mux4Way1Bit()
        mux4way1bit_1_out = mux4way1bit_1.compute(sel[1:], a, b, c, d)

        mux4way1bit_2 = Mux4Way1Bit()
        mux4way1bit_2_out = mux4way1bit_2.compute(sel[1:], e, f, g, h)

        mux2way1bit = Mux2Way1Bit()
        mux2way1bit_out = mux2way1bit.compute(sel[0], mux4way1bit_1_out, mux4way1bit_2_out)

        return mux2way1bit_out
