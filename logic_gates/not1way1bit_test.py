import sys
from not1way1bit import Not1Way1Bit

test_input = [0,1]
test_output = [1,0]

not1Way1Bit = Not1Way1Bit()

for i in range(len(test_input)):
    result = not1Way1Bit.compute(test_input[i])
    if result != test_output[i]:
        sys.exit('Error, in[{}] should output: [{}] but got: [{}]'.format(test_input[i], test_output[i], result))
print("Test for Not1Way1Bit passed successfully.")
