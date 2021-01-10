from dmux2way16bit import DMux2Way16Bit
from dmux4way16bit import DMux4Way16Bit


class DMux8Way16Bit:

    def compute(self, sel, _in):

        assert len(sel) == 3

        dMux2Way = DMux2Way16Bit()
        dMux4Way_1 = DMux4Way16Bit()
        dMux4Way_2 = DMux4Way16Bit()

        dMux2Way_out = dMux2Way.compute(sel[0], _in)
        dMux4Way_1_out = dMux4Way_1.compute(sel[1:], dMux2Way_out[0])
        dMux4Way_2_out = dMux4Way_2.compute(sel[1:], dMux2Way_out[1])

        return dMux4Way_1_out + dMux4Way_2_out
