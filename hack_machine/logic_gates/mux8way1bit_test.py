import sys
from mux8way1bit import Mux8Way1Bit

test_a_input = [1,0,0,0,0,0,0,0]
test_b_input = [0,1,0,0,0,0,0,0]
test_c_input = [0,0,1,0,0,0,0,0]
test_d_input = [0,0,0,1,0,0,0,0]
test_e_input = [0,0,0,0,1,0,0,0]
test_f_input = [0,0,0,0,0,1,0,0]
test_g_input = [0,0,0,0,0,0,1,0]
test_h_input = [0,0,0,0,0,0,0,1]

test_sel_input = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]

test_output = [1,1,1,1,1,1,1,1]

mux8Way1Bit = Mux8Way1Bit()

for i in range(len(test_a_input)):
    result = mux8Way1Bit.compute(test_sel_input[i], test_a_input[i], test_b_input[i], test_c_input[i], test_d_input[i],
                                                     test_e_input[i], test_f_input[i], test_g_input[i], test_h_input[i])

    if result != test_output[i]:
        sys.exit('Error, the input sel{}, a{}, b{}, c{}, d{}, e{}, f{}, g{}, h{} should output: {} but instead got: {}'
           .format(test_sel_input[i], test_a_input[i], test_b_input[i], test_c_input[i], test_d_input[i],
                                      test_e_input[i], test_f_input[i], test_g_input[i], test_h_input[i],
                                      test_output[i], result))

print("Test for Mux8Way1Bit passed successfully.")
