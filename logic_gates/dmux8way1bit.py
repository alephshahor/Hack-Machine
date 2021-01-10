from dmux2way1bit import DMux2Way1Bit
from dmux4way1bit import DMux4Way1Bit


class DMux8Way1Bit:

    def compute(self, sel, _in):

        assert len(sel) == 3

        dMux2Way = DMux2Way1Bit()
        dMux4Way_1 = DMux4Way1Bit()
        dMux4Way_2 = DMux4Way1Bit()

        dMux2Way_out = dMux2Way.compute(sel[0], _in)
        dMux4Way_1_out = dMux4Way_1.compute(sel[1:], dMux2Way_out[0])
        dMux4Way_2_out = dMux4Way_2.compute(sel[1:], dMux2Way_out[1])

        return dMux4Way_1_out + dMux4Way_2_out
