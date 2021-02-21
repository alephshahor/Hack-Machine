import sys
from ram4kbit import RAM4KBit
sys.path.append('../logic_gates')
from mux4way16bit import Mux4Way16Bit
from dmux4way1bit import DMux4Way1Bit

class RAM16KBit:

    def __init__(self):
        self.rams = [RAM4KBit() for i in range(4)]

    def compute(self, _in, address, load):

        assert len(_in) == 16
        assert len(address) == 14

        ram_selector = address[:2]
        instr_selector = address[2:]

        load_dmux = DMux4Way1Bit()
        load_dmux_out = load_dmux.compute(ram_selector, load)

        ram_0_out = self.rams[0].compute(_in, instr_selector, load_dmux_out[0])
        ram_1_out = self.rams[1].compute(_in, instr_selector, load_dmux_out[1])
        ram_2_out = self.rams[2].compute(_in, instr_selector, load_dmux_out[2])
        ram_3_out = self.rams[3].compute(_in, instr_selector, load_dmux_out[3])

        output_mux = Mux4Way16Bit()
        output_mux_out = output_mux.compute(ram_selector,
                                            ram_0_out,
                                            ram_1_out,
                                            ram_2_out,
                                            ram_3_out)

        return output_mux_out
