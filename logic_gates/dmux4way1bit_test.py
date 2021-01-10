import sys
from dmux4way1bit import DMux4Way1Bit

test_input = [1,1,1,1]
test_sel = [[0,0],[0,1],[1,0],[1,1]]
test_output = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

dMux4Way1Bit = DMux4Way1Bit()

for i in range(len(test_input)):
    result = dMux4Way1Bit.compute(test_sel[i], test_input[i])
    if result != test_output[i]:
        sys.exit('Error, sel{}, in{} should output: {} but got: {}'
           .format(test_sel[i], test_input[i], test_output[i], result))
print("Test for Dmux4Way1Bit passed successfully.")
