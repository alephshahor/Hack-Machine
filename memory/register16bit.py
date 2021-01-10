from bit import Bit

class Register16Bit:

    def __init__(self):
        self.bits = [Bit() for i in range(16)]

    def compute(self, _in, load):

        assert len(_in) == 16

        reg_out = [0] * 16
        for i in range(16):
            bit_out = self.bits[i].compute(_in[i], load)
            reg_out[i] = bit_out

        return reg_out
