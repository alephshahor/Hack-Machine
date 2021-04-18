import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/alu')
from add16bit import Add16Bit

from register16bit import Register16Bit


# TODO: This should be done with logic gates.
class Pc:

    def __init__(self):
        self.register = Register16Bit()
        self.adder = Add16Bit()

    def compute(self, _in, inc, load, reset):

        if reset == 1:
            zero = [0] * 16
            return self.register.compute(zero, 1)
        elif load == 1:
            return self.register.compute(_in, 1)
        elif inc == 1:
            current_instr = self.register.value()
            one = [0] * 15 + [1]
            next_instr = self.adder.compute(current_instr, one)
            return self.register.compute(next_instr, 1)
        else:
            return self.register.value()
