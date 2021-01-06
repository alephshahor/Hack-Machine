import sys
from or2x1 import Or2x1

test_input = [[0,0,0], [0,1,1], [1,0,1], [1,1,1]]
or2x1 = Or2x1()

for t_input in test_input:
    if or2x1.compute(t_input[0], t_input[1]) != t_input[2]:
        sys.exit('Error, the inputs {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2]))
print("Test for Or2x1 passed successfully.")
