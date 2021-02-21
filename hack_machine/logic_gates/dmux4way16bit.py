from hack_machine.logic_gates.dmux2way16bit import DMux2Way16Bit

class DMux4Way16Bit:

    def compute(self, sel, _in):

        assert len(sel) == 2
        assert len(_in) == 16

        dMux2Way_1 = DMux2Way16Bit()
        dMux2Way_2 = DMux2Way16Bit()
        dMux2Way_3 = DMux2Way16Bit()

        dMux2Way_1_out = dMux2Way_1.compute(sel[0], _in)
        dMux2Way_2_out = dMux2Way_1.compute(sel[1], dMux2Way_1_out[0])
        dMux2Way_3_out = dMux2Way_1.compute(sel[1], dMux2Way_1_out[1])

        return dMux2Way_2_out + dMux2Way_3_out
