import sys
from mux16x1 import Mux16x1

test_input = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],[1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0]]
test_output = [1, 1, 1, 1]
mux16x1 = Mux16x1()
for i in range(len(test_input)):
    sel = list("{0:04b}".format(i))
    result = mux16x1.compute(sel, test_input[i])
    if result != test_output[i]:
        sys.exit('Error, the input {} - {} should output: {}'.format(sel, test_input[i], test_output[i]))
print("Test for Mux16x1 passed successfully.")

