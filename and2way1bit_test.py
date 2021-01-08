import sys
from and2way1bit import And2Way1Bit

test_input = [[0,0,0], [0,1,0], [1,0,0], [1,1,1]]
and2Way1bit = And2Way1Bit()

for t_input in test_input:
    result = and2Way1bit.compute(t_input[0], t_input[1])
    if result != t_input[2]:
        sys.exit('Error, the inputs {} - {}  should output: {}'.format(t_input[0], t_input[1], t_input[2]))
print("Test for And2Way1bit passed successfully.")
