import sys

sys.path.append('../logic_gates')
from xor2way1bit import Xor2Way1Bit
from and2way1bit import And2Way1Bit

class HalfAdder:

    def compute(self, a, b):

        xor2Way1Bit = Xor2Way1Bit()
        and2Way1Bit = And2Way1Bit()

        xor_out = xor2Way1Bit.compute(a,b)
        and_out = and2Way1Bit.compute(a,b)

        return xor_out, and_out
