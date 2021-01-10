import sys
from register16bit import Register16Bit
sys.path.append('../logic_gates')
from mux8way16bit import Mux8Way16Bit
from dmux8way1bit import DMux8Way1Bit

class RAM8Bit:

    def __init__(self):
        self.registers = [Register16Bit() for i in range(8)]

    def print_memory(self):
        for register in self.registers:
            register.print_register()
        print("\n\n")

    def compute(self, _in, address, load):

        assert len(_in) == 16
        assert len(address) == 3


        load_dmux = DMux8Way1Bit()
        load_dmux_out = load_dmux.compute(address, load)

        reg_0_out = self.registers[0].compute(_in, load_dmux_out[0])
        reg_1_out = self.registers[1].compute(_in, load_dmux_out[1])
        reg_2_out = self.registers[2].compute(_in, load_dmux_out[2])
        reg_3_out = self.registers[3].compute(_in, load_dmux_out[3])
        reg_4_out = self.registers[4].compute(_in, load_dmux_out[4])
        reg_5_out = self.registers[5].compute(_in, load_dmux_out[5])
        reg_6_out = self.registers[6].compute(_in, load_dmux_out[6])
        reg_7_out = self.registers[7].compute(_in, load_dmux_out[7])

        output_mux = Mux8Way16Bit()
        output_mux_out = output_mux.compute(address,
                                            reg_0_out,
                                            reg_1_out,
                                            reg_2_out,
                                            reg_3_out,
                                            reg_4_out,
                                            reg_5_out,
                                            reg_6_out,
                                            reg_7_out)

        return output_mux_out
