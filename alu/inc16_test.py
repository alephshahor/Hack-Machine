import sys
from inc16 import Inc16


test_input = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0], [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
test_output= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

inc16 = Inc16()

for i in range(len(test_input)):

    result = inc16.compute(test_input[i])

    if result != test_output[i]:
        sys.exit('Error, in{} should output {} but got: {}'
           .format(test_input[i], test_output[i], result))

print("Test for Inc16 passed successfully.")
