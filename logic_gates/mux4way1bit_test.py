import sys
from mux4way1bit import Mux4Way1Bit

test_a_input = [1,0,0,0]
test_b_input = [0,1,0,0]
test_c_input = [0,0,1,0]
test_d_input = [0,0,0,1]

test_sel_input = [[0,0], [0,1], [1,0], [1,1]]

test_output = [1,1,1,1]

mux4Way1Bit = Mux4Way1Bit()

for i in range(len(test_a_input)):
    result = mux4Way1Bit.compute(test_sel_input[i], test_a_input[i], test_b_input[i], test_c_input[i], test_d_input[i])

    if result != test_output[i]:
        sys.exit('Error, the input sel{}, a{}, b{}, c{}, d{} should output: {} but instead got: {}'
           .format(test_sel_input[i], test_a_input[i], test_b_input[i], test_c_input[i], test_d_input[i], test_output[i], result))

print("Test for Mux4Way1Bit passed successfully.")
