import sys
from not1way16bit import Not1Way16Bit

test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
test_output = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

not1Way16Bit = Not1Way16Bit()

for i in range(len(test_input)):
    if not1Way16Bit.compute(test_input[i]) != test_output[i]:
        sys.exit('Error, the input {} should output: {}'.format(test_input[i], test_output[i]))
print("Test for Not1Way16Bit passed successfully.")
