import sys
from ram64bit import RAM64Bit
sys.path.append('../logic_gates')
from mux8way16bit import Mux8Way16Bit
from dmux8way1bit import DMux8Way1Bit

class RAM512Bit:

    def __init__(self):
        self.rams = [RAM64Bit() for i in range(8)]

    def compute(self, _in, address, load):

        assert len(_in) == 16
        assert len(address) == 9 

        ram_selector = address[:3]
        instr_selector = address[3:]

        load_dmux = DMux8Way1Bit()
        load_dmux_out = load_dmux.compute(ram_selector, load)

        ram_0_out = self.rams[0].compute(_in, instr_selector, load_dmux_out[0])
        ram_1_out = self.rams[1].compute(_in, instr_selector, load_dmux_out[1])
        ram_2_out = self.rams[2].compute(_in, instr_selector, load_dmux_out[2])
        ram_3_out = self.rams[3].compute(_in, instr_selector, load_dmux_out[3])
        ram_4_out = self.rams[4].compute(_in, instr_selector, load_dmux_out[4])
        ram_5_out = self.rams[5].compute(_in, instr_selector, load_dmux_out[5])
        ram_6_out = self.rams[6].compute(_in, instr_selector, load_dmux_out[6])
        ram_7_out = self.rams[7].compute(_in, instr_selector, load_dmux_out[7])

        output_mux = Mux8Way16Bit()
        output_mux_out = output_mux.compute(ram_selector,
                                            ram_0_out,
                                            ram_1_out,
                                            ram_2_out,
                                            ram_3_out,
                                            ram_4_out,
                                            ram_5_out,
                                            ram_6_out,
                                            ram_7_out)

        return output_mux_out
