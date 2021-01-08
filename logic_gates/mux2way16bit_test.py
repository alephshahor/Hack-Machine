import sys
from mux2way16bit import Mux2Way16Bit

test_a_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]]
test_b_input = [[1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]
test_sel_input = [0,1]

test_output = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]

mux2Way16Bit = Mux2Way16Bit()

for i in range(len(test_a_input)):
    result = mux2Way16Bit.compute(test_sel_input[i], test_a_input[i], test_b_input[i])

    if result != test_output[i]:
        sys.exit('Error, the input sel{}, a{}, b{} should output: {} but instead got: {}'
           .format(test_sel_input[i], test_a_input[i], test_b_input[i], test_output[i], result))

print("Test for Mux2Way16Bit passed successfully.")
