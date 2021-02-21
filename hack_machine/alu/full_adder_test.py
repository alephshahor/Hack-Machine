import sys
from full_adder import FullAdder

test_input = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
test_output = [[0,0],[1,0],[1,0],[0,1],[1,0],[0,1],[0,1],[1,1]]

full_adder = FullAdder()

for i in range(len(test_input)):
    a = test_input[i][0]
    b = test_input[i][1]
    c = test_input[i][2]

    sum, carry = full_adder.compute(a,b,c)

    if sum != test_output[i][0] or carry != test_output[i][1]:
        sys.exit('Error, a[{}], b[{}], c[{}] should output [{}], [{}] but got: [{}]. [{}]'
           .format(a,b,c,test_output[i][0], test_output[i][1], sum, carry))

print("Test for FullAdder passed successfully.")
