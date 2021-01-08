import sys
from not16x16 import Not16x16

test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
test_output = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
not16x16 = Not16x16()
for i in range(len(test_input)):
    if not16x16.compute(test_input[i]) != test_output[i]:
        sys.exit('Error, the input {} should output: {}'.format(test_input[i], test_output[i]))
print("Test for Not16x16 passed successfully.")

