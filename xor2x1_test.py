import sys
from xor2x1 import Xor2x1

test_input = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]]
xor2x1 = Xor2x1()

for t_input in test_input:
    if xor2x1.compute(t_input[0], t_input[1]) != t_input[2]:
        sys.exit('Error, the inputs {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2]))
print("Test for Xor2x1 passed successfully.")
