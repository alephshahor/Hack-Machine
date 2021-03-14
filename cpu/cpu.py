import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way16bit import Mux2Way16Bit
from mux2way1bit import Mux2Way1Bit

sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from ram32kbit import RAM32KBit
from register16bit import Register16Bit
from pc import Pc

sys.path.append(os.environ['ROOT_FOLDER'] + '/alu')
from alu import Alu

sys.path.append(os.environ['ROOT_FOLDER'] + '/cpu')
from decoder import Decoder
from jump_decoder import JumpDecoder

zero = [0] * 16
one = zero[:15] + [1]

# TODO: Decoder fuera!
class CPU:

    def __init__(self):
        #instruction_memory = RAM32KBit()
        #data_memory = RAM32KBit()
        self.decoder = Decoder()
        self.alu = Alu()
        self.a_register = Register16Bit()
        self.d_register = Register16Bit()
        self.jump_decoder = JumpDecoder()
        self.pc = Pc()
        self.a_out = zero
        self.d_out = zero
        self.alu_out = zero
        self.jump_decoder_out = 0 # Lo puedes quitar de aqui creo
        self.load_pc = 0
        self.a_or_c_instr_mux = Mux2Way16Bit()
        self.load_a_mux = Mux2Way1Bit()
        self.a_or_m_mux = Mux2Way16Bit()
        self.load_d_mux = Mux2Way1Bit()
        self.load_jump_mux = Mux2Way1Bit()

    def compute(self, instr, mem_in, reset):
        
        x, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = self.decoder.compute(instr)

        a_in = self.a_or_c_instr_mux.compute(x, instr, self.alu_out)
        a_load = self.load_a_mux.compute(x, 1, d1)
        self.a_out = self.a_register.compute(a_in, a_load)

        a_or_m_mux_out = self.a_or_m_mux.compute(a, self.a_out, mem_in)
        self.alu_out = self.alu.compute(c1, c2, c3, c4, c5, c6, self.d_out, a_or_m_mux_out)

        self.jump_decoder_out = self.jump_decoder.compute(self.alu_out, j1,j2,j3)
        self.load_pc = self.load_jump_mux.compute(x, 0, self.jump_decoder_out)
        instr_dir = self.pc.compute(self.a_out, 1, self.load_pc, reset)
        d_load = self.load_d_mux.compute(x, 0, d2)
        self.d_out = self.d_register.compute(self.alu_out, d_load)

        mem_dir = self.a_out

        return self.alu_out, instr_dir, mem_dir
