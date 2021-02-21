import sys
from dmux2way1bit import DMux2Way1Bit

test_input = [1,1]
test_sel = [0,1]
test_output = [[1,0],[0,1]]

dMux2Way1Bit = DMux2Way1Bit()

for i in range(len(test_input)):
    result = dMux2Way1Bit.compute(test_sel[i], test_input[i])
    if result != test_output[i]:
        sys.exit('Error, sel[{}], in[{}] should output: {} but got: {}'
           .format(test_sel[i], test_input[i], test_output[i], result))
print("Test for Dmux2Way1bit passed successfully.")
