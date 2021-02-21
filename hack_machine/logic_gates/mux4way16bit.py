from mux2way16bit import Mux2Way16Bit

class Mux4Way16Bit:

    def compute(self, sel, a, b, c, d):

        assert len(sel) == 2

        assert len(a) == 16
        assert len(b) == 16
        assert len(c) == 16
        assert len(d) == 16

        sel_str = ''.join(str(bit) for bit in sel)

        mux2Way16Bit_1 = Mux2Way16Bit()
        mux2Way16Bit_2 = Mux2Way16Bit()
        mux2Way16Bit_3 = Mux2Way16Bit()

        mux2Way16Bit_1_out = mux2Way16Bit_1.compute(sel[1], a, b)
        mux2Way16Bit_2_out = mux2Way16Bit_2.compute(sel[1], c, d)
        mux2Way16Bit_3_out = mux2Way16Bit_3.compute(sel[0], mux2Way16Bit_1_out, mux2Way16Bit_2_out)

        return mux2Way16Bit_3_out
