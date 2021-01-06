import sys
from nand2x1 import Nand2x1

test_input = [[0,0,1], [0,1,1], [1,0,1], [1,1,0]]
nand = Nand2x1()

for t_input in test_input:
    if nand.compute(t_input[0], t_input[1]) != t_input[2]:
        sys.exit('Error, the inputs {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2]))
print("Test for Nand2x1 passed successfully.")
