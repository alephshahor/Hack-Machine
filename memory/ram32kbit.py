import sys
from ram16kbit import RAM16KBit
sys.path.append('../logic_gates')
from mux2way16bit import Mux2Way16Bit
from dmux2way1bit import DMux2Way1Bit




class RAM32KBit:

    def __init__(self):
        self.rams = [RAM16KBit() for i in range(2)]

    def compute(self, _in, address, load):

        assert len(_in) == 16
        assert len(address) == 15

        ram_selector = address[0]
        instr_selector = address[1:]
        
        load_dmux = DMux2Way1Bit()
        load_dmux_out = load_dmux.compute(ram_selector, load)

        ram_0_out = self.rams[0].compute(_in, instr_selector, load_dmux_out[0])
        ram_1_out = self.rams[1].compute(_in, instr_selector, load_dmux_out[1])
        output_mux = Mux2Way16Bit()
        output_mux_out = output_mux.compute(ram_selector,
                                            ram_0_out,
                                            ram_1_out)
        return output_mux_out
