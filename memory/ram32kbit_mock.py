import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

mem_size = pow(2, 15)

class RAM32KMock:

    def __init__(self):
        self.mem = [[0] * 16] * mem_size

    def compute(self, _in, address, load):
        address = conversions.bin_arr_to_dec(address)

        selected_reg_data = self.mem[address]

        if load:
            self.mem[address] = _in

        return selected_reg_data