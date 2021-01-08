import sys
from or8way1bit import Or8Way1Bit

test_input = [[0,1,0,0,0,0,1,0], [0,0,0,0,0,0,0,0], [0,1,1,0,0,0,1,1]]

test_output = [1,0,1]

or8Way1Bit = Or8Way1Bit()

for i in range(len(test_input)):
    result = or8Way1Bit.compute(test_input[i])

    if result != test_output[i]:
        sys.exit('Error, in{} should output: {} but instead got: {}'
           .format(test_input[i], test_output[i], result))

print("Test for Or8Way1Bit passed successfully.")
