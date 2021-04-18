import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from ram32kbit_mock import RAM32KMock

sys.path.append(os.environ['ROOT_FOLDER'] + '/cpu')
from decoder import Decoder
from cpu import CPU

zero = [0] * 16

class Emulator:
    
    def __init__(self):
        self.cpu = CPU()
        self.data_memory = RAM32KMock()
        self.instruction_memory = RAM32KMock()
        self.decoder = Decoder()
        self.instr_dir = zero
        self.load_pc = 0
        self.load_mem = 0
        self.alu_out = zero

    def load_instructions_mock(self, instructions):
        for i, instr in enumerate(instructions):
            self.instruction_memory.mem[i] = instr

    def run(self, n_iterations):

        for _ in range(n_iterations):

            instr_addr = self.cpu.pc.register.value()
            instr = self.instruction_memory.compute(zero, instr_addr, 0)

            mem_in = self.data_memory.compute(self.alu_out, self.cpu.a_register.value(), self.load_mem)
            alu_out, load_pc, _ = self.cpu.compute(instr, mem_in)

            self.alu_out = alu_out

            self.cpu.pc.compute(self.cpu.a_register.value(), 1, load_pc, 0)

            x, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = self.decoder.compute(instr)
            self.load_mem = d3



