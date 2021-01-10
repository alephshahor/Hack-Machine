import sys
from ram8bit import RAM8Bit

test_input      = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
test_load       = [1,                                  0,                                 1,                                 1,                                 1]
test_address    = [[0,0,0],                           [0,0,0],                           [0,0,1],                           [0,0,1],                           [0,0,0]]
test_output     = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]]

ram8Bit = RAM8Bit()

for i in range(len(test_input)):

    result = ram8Bit.compute(test_input[i], test_address[i], test_load[i])
    if result != test_output[i]:
        sys.exit('Error, in[{}], address[{}], load[{}] should output: [{}] but got: [{}]'
           .format(test_input[i-1], test_load[i-1], test_address[i-1], test_output[i], result))

print("Test for RAM8Bit passed successfully.")
