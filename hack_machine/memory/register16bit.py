from bit import Bit

class Register16Bit:

    def __init__(self):
        self.bits = [Bit() for i in range(16)]

    def print_register(self):
        bits = []
        for bit in self.bits:
            bits.append(bit.dff.internal_state)
        print(bits)

    def compute(self, _in, load):

        assert len(_in) == 16

        reg_out = [0] * 16
        for i in range(16):
            bit_out = self.bits[i].compute(_in[i], load)
            reg_out[i] = bit_out

        return reg_out
