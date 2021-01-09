import sys
from dmux2way import DMux2Way

test_input = [[0,0], [0,1], [1,0], [1,1]]
test_output = [[0,0],[1,0],[0,0],[0,1]]

dMux2Way = DMux2Way()

for i in range(len(test_input)):
    result = dMux2Way.compute(test_input[i][0], test_input[i][1])
    if result != test_output[i]:
        sys.exit('Error, sel[{}], in[{}] should output: {} but got: {}'
           .format(test_input[i][0], test_input[i][1], test_output[i], result))
print("Test for Dmux2Way1Bit passed successfully.")
