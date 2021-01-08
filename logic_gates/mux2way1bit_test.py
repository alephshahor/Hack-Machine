import sys
from mux2way1bit import Mux2Way1Bit

test_input = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
test_output = [0,0,1,1,0,1,0,1]

mux2Way1Bit = Mux2Way1Bit()

for i in range(len(test_input)):
    result = mux2Way1Bit.compute(test_input[i][0], test_input[i][1], test_input[i][2])
    if result != test_output[i]:
        sys.exit('Error, sel[{}], a[{}], b[{}] should output: [{}] but got: [{}]'
           .format(test_input[i][0], test_input[i][1], test_input[i][2], test_output[i], result))
print("Test for Mux2Way1Bit passed successfully.")
