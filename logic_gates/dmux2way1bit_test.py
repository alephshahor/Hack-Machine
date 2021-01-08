import sys
from dmux2way1bit import DMux2Way1Bit

test_input = [[0,0], [0,1], [1,0], [1,1]]
test_output = [[0,0],[1,0],[0,0],[0,1]]

dMux2Way1Bit = DMux2Way1Bit()

for i in range(len(test_input)):
    result = dMux2Way1Bit.compute(test_input[i][0], test_input[i][1])
    if result != test_output[i]:
        sys.exit('Error, sel[{}], in[{}] should output: {} but got: {}'
           .format(test_input[i][0], test_input[i][1], test_output[i], result))
print("Test for Dmux2Way1Bit passed successfully.")
