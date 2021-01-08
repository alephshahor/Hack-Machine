import sys
from and2way16bit import And2Way16Bit

a_test_input = [[0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0]]
b_test_input = [[0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1]]
test_output  = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]]

and2Way16Bit = And2Way16Bit()

for i in range(len(a_test_input)):
    result = and2Way16Bit.compute(a_test_input[i], b_test_input[i])
    if result != test_output[i]:
        sys.exit('Error, a[{}], b[{}] should output: [{}] but got: [{}]'.format(a_test_input[i], b_test_input[i], test_output[i], result))
print("Test for And2Way16Bit passed successfully.")
