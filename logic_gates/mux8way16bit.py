import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux4way16bit import Mux4Way16Bit
from mux2way16bit import Mux2Way16Bit

class Mux8Way16Bit:

    def compute(self, sel, a, b, c, d, e, f, g, h):

        assert len(sel) == 3

        assert len(a) == 16
        assert len(b) == 16
        assert len(c) == 16
        assert len(d) == 16
        assert len(e) == 16
        assert len(f) == 16
        assert len(g) == 16
        assert len(h) == 16

        mux4Way16Bit_1 = Mux4Way16Bit()
        mux4Way16Bit_2 = Mux4Way16Bit()
        mux2Way16Bit_3 = Mux2Way16Bit()

        mux4Way16Bit_1_out = mux4Way16Bit_1.compute(sel[1:], a, b, c, d)
        mux4Way16Bit_2_out = mux4Way16Bit_2.compute(sel[1:], e, f, g, h)
        mux2Way16Bit_3_out = mux2Way16Bit_3.compute(sel[0], mux4Way16Bit_1_out, mux4Way16Bit_2_out)

        return mux2Way16Bit_3_out
