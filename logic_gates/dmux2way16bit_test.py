import sys
from dmux2way16bit import DMux2Way16Bit

test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
test_sel = [0, 1]
test_output = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]]

dMux2Way16Bit = DMux2Way16Bit()

for i in range(len(test_input)):
    result = dMux2Way16Bit.compute(test_sel[i], test_input[i])
    if result != test_output[i]:
        sys.exit('Error, sel[{}], in{} should output: {} but got: {}'
           .format(test_sel[i], test_input[i], test_output[i], result))
print("Test for Dmux2Way16bit passed successfully.")
