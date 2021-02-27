import pytest
from ram32kbit import RAM32KBit

test_input = [i + 1 for i in range(16)] 
test_load = ([1] * 8) + ([0] * 8)
test_result = ([0] * 8) + [i + 1 for i in range(8)]

ram32kBit = RAM32KBit()

def to_binary_arr(num, n_bits):
    bin_str_format = "{0:0"+str(n_bits)+"b}"
    bin_num_str = bin_str_format.format(num)
    bin_num_str_arr = list(bin_num_str)
    bin_num_arr = [ int(bit) for bit in bin_num_str_arr ]
    return bin_num_arr

def test_ram32kbit():

    for j in range(2):
        offset = 0
        if j == 1:
            offset = 8
        test_address = [ i + ( 16384 * (j + 1) - offset) for i in range(8) ] * 2
        for i in range(len(test_input)):
            _in  = to_binary_arr(test_input[i], 16)
            addr = to_binary_arr(test_address[i], 15)
            load = test_load[i]
            result = ram32kBit.compute(_in, addr, load)
            exp_result = to_binary_arr(test_result[i], 16)

            assert result == exp_result, 'Error, in: {}, address: {}, load: {} should output: {} but got: {}'.format(_in,
                                                                                                                     addr,
                                                                                                                     load,
                                                                                                                     exp_result,
                                                                                                                     result)


