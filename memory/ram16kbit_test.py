import sys
from ram16kbit import RAM16KBit

test_input = [i + 1 for i in range(16)] 
test_load = ([1] * 8) + ([0] * 8)
test_result = ([0] * 8) + [i + 1 for i in range(8)]

ram16kBit = RAM16KBit()

def to_binary_arr(num, n_bits):
    bin_str_format = "{0:0"+str(n_bits)+"b}"
    bin_num_str = bin_str_format.format(num)
    bin_num_str_arr = list(bin_num_str)
    bin_num_arr = [ int(bit) for bit in bin_num_str_arr ]
    return bin_num_arr

for j in range(4):
    offset = 0
    if j == 3:
        offset = 8
    test_address = [ i + ( 4096 * (j + 1) - offset) for i in range(8) ] * 2
    for i in range(len(test_input)):
        _in  = to_binary_arr(test_input[i], 16)
        addr = to_binary_arr(test_address[i], 14)
        load = test_load[i]
        result = ram16kBit.compute(_in, addr, load)
        exp_result = to_binary_arr(test_result[i], 16)

        if result != exp_result:
            sys.exit('Error, in[{}], address[{}], load[{}] should output: [{}] but got: [{}]'
               .format(_in, addr, load, exp_result, result))
    print("Memory " + str(j) + " passed successfully")
print("Test for RAM16KBit passed successfully")


