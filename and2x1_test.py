import sys
from and2x1 import And2x1

test_input = [[0,0,0], [0,1,0], [1,0,0], [1,1,1]]
and2x1 = And2x1()

for t_input in test_input:
    if and2x1.compute(t_input[0], t_input[1]) != t_input[2]:
        sys.exit('Error, the inputs {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2]))
print("Test for And2x1 passed successfully.")
