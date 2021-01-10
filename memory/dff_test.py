import sys
from dff import DFF

test_input = [0,1,0,1]
test_output = [0,0,1,0]

dff = DFF()

for i in range(len(test_input)):

    result = dff.compute(test_input[i])
    if result != test_output[i]:
        sys.exit('Error, in[{}], should output: [{}] but got: [{}]'
           .format(test_input[i], test_output[i], result))
           
print("Test for DFF passed successfully.")
