import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from xor2way1bit import Xor2Way1Bit
from and2way1bit import And2Way1Bit

class HalfAdder:

    def compute(self, a, b):

        xor2Way1Bit = Xor2Way1Bit()
        and2Way1Bit = And2Way1Bit()

        sum = xor2Way1Bit.compute(a,b)
        carry = and2Way1Bit.compute(a,b)

        return sum, carry
