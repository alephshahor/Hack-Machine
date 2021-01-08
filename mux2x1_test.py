import sys
from mux2x1 import Mux2x1

test_input = [[0,0,0,0],[0,0,1,0],[0,1,0,1],[0,1,1,1],[1,0,0,0], [1,0,1,1], [1,1,0,0], [1,1,1,1]]
mux2x1 = Mux2x1()

for t_input in test_input:
    if mux2x1.compute(t_input[0], t_input[1], t_input[2]) != t_input[3]:
        sys.exit('Error, the inputs {} - {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2], t_input[3]))
print("Test for Mux2x1 passed successfully.")
