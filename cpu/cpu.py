import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way16bit import Mux2Way16Bit

sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from ram32kbit import RAM32KBit
from register16bit import Register16Bit
from pc import Pc

sys.path.append(os.environ['ROOT_FOLDER'] + '/alu')
from cpu import Alu
from jumpdecoder import JumpDecoder

sys.path.append(os.environ['ROOT_FOLDER'] + '/cpu')
from decoder import Decoder

zero = [0] * 16
one = zero[:15] + [1]

instruction_memory = RAM32KBit()
data_memory = RAM32KBit()
decoder = Decoder()
alu = Alu()
a_register = Register16Bit()
d_register = Register16Bit()
jump_decoder = JumpDecoder()
pc = Pc()

a_out = zero
d_out = zero
alu_out = zero
jump_decoder_out = 0

a_or_c_instr_mux = Mux2Way16Bit()
load_a_mux = Mux2Way16Bit()
a_or_m_mux = Mux2Way16Bit()
load_d_mux = Mux2Way16Bit()

instr_dir = pc.compute(a_out, 1, jump_decoder_out, 0)
instr = instruction_memory.compute(zero, instr_dir, 0)
mem_in = data_memory.compute(alu_out, a_out, d3)
x, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = decoder.compute(instr)

a_in = a_or_c_instr_mux.compute(x, alu_out, instr)
a_load = load_a_mux.compute(x, one, d1)
a_out = a_register.compute(a_in, a_load)

a_or_m_mux_out = a_or_m_mux.compute(a, a_in, mem_in)
alu_out = alu.compute(c1, c2, c3, c4, c5, c6, a_out, d_out)

jump_decoder_out = jump_decoder.compute(alu_out, j1,j2,j3)

d_load = load_d_mux.compute(x, zero, d2)
d_out = d_register.compute(alu_out, d_load)

