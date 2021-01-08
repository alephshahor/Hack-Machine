import sys
from or16x1 import Or16x1

test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],[1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0]]
test_output = [0, 1, 1, 1]
or16x1 = Or16x1()
for i in range(len(test_input)):
    if or16x1.compute(test_input[i]) != test_output[i]:
        sys.exit('Error, the input {} should output: {}'.format(test_input[i], test_output[i]))
print("Test for Or16x1 passed successfully.")

