from dmux2way import DMux2Way
from dmux4way import DMux4Way


class DMux8Way:

    def compute(self, sel, _in):

        assert len(sel) == 3

        dMux2Way = DMux2Way()
        dMux4Way_1 = DMux4Way()
        dMux4Way_2 = DMux4Way()

        dMux2Way_out = dMux2Way.compute(sel[0], _in)
        dMux4Way_1_out = dMux4Way_1.compute(sel[1:], dMux2Way_out[0])
        dMux4Way_2_out = dMux4Way_2.compute(sel[1:], dMux2Way_out[1])

        return dMux4Way_1_out + dMux4Way_2_out
