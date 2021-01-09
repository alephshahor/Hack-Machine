import sys
from dmux4way import DMux4Way

test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]
test_sel = [[0,0],[0,1],[1,0],[1,1]]
test_output = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],0,0,0],
               [0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0,0],
               [0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],0],
               [0,0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]]

dMux4Way = DMux4Way()

for i in range(len(test_input)):
    result = dMux4Way.compute(test_sel[i], test_input[i])
    if result != test_output[i]:
        sys.exit('Error, sel{}, in{} should output: {} but got: {}'
           .format(test_sel[i], test_input[i], test_output[i], result))
print("Test for Dmux4Way passed successfully.")
