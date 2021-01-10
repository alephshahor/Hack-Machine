from mux4way1bit import Mux4Way1Bit
from mux2way1bit import Mux2Way1Bit

class Mux8Way1Bit:

    def compute(self, sel, a, b, c, d, e, f, g, h):

        assert len(sel) == 3

        mux4Way1Bit_1 = Mux4Way1Bit()
        mux4Way1Bit_2 = Mux4Way1Bit()
        mux2Way1Bit_3 = Mux2Way1Bit()

        mux4Way1Bit_1_out = mux4Way1Bit_1.compute(sel[1:], a, b, c, d)
        mux4Way1Bit_2_out = mux4Way1Bit_2.compute(sel[1:], e, f, g, h)
        mux2Way1Bit_3_out = mux2Way1Bit_3.compute(sel[0], mux4Way1Bit_1_out, mux4Way1Bit_2_out)

        return mux2Way1Bit_3_out
