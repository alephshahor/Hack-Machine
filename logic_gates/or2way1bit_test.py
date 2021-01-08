import sys
from or2way1bit import Or2Way1Bit

test_input = [[0,0], [0,1], [1,0], [1,1]]
test_output = [0,1,1,1]
or2way1bit = Or2Way1Bit()

for i in range(len(test_input)):
    result = or2way1bit.compute(test_input[i][0], test_input[i][1])
    if result != test_output[i]:
        sys.exit('Error, a[{}], b[{}] should output: [{}] but got: [{}]'.format(test_input[i][0], test_input[i][1], test_output[i], result))
print("Test for Or2Way1Bit passed successfully.")
