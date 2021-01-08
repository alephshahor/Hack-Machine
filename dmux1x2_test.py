import sys
from dmux1x2 import DMux1x2

test_input = [[0,0,0,0], [0,1,1,0], [1,0,0,0], [1,1,0,1]]
dmux1x2 = DMux1x2()

for t_input in test_input:
    if dmux1x2.compute(t_input[0], t_input[1]) != (t_input[2] ,t_input[3]):
        sys.exit('Error, the inputs {} - {}  should output: {} - {}'.format(t_input[0], t_input[1], t_input[2], t_input[3]))
print("Test for Dmux1x2 passed successfully.")

