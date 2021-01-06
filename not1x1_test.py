import sys
from not1x1 import Not1x1

test_input = [[0,1], [1,0]]
not1x1 = Not1x1()
for t_input in test_input:
    if not1x1.compute(t_input[0]) != t_input[1]:
        sys.exit('Error, the input {} should output: {}'.format(t_input[0], t_input[1]))
print("Test for Not1x1 passed successfully.")

