import sys
from alu import Alu

alu = Alu()

# ZERO
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 0
zy = 1
ny = 0
f  = 1
no = 0

out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.zero(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# ONE
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 1
ny = 1
f  = 1
no = 1

out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# MINUS ONE
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 1
ny = 0
f  = 1
no = 0

out = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.minus_one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 1
ny = 1
f  = 0
no = 0

out = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 0
ny = 0
f  = 0
no = 0

out = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# NOT X
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 1
ny = 1
f  = 0
no = 1

out = [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.not_x(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))


# NOT Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 0
ny = 0
f  = 0
no = 1

out = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.not_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# -X
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] # 54613
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] # 43690

zx = 0
nx = 0
zy = 1
ny = 1
f  = 1
no = 1

out = [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]


result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.minus_x(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))
# -Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 0
ny = 0
f  = 1
no = 1

out = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.minus_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X + 1
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 1
zy = 1
ny = 1
f  = 1
no = 1

out = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_plus_one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# Y + 1
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 0
ny = 1
f  = 1
no = 1

out = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.y_plus_one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))


# X - 1
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 1
ny = 1
f  = 1
no = 0

out = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_minus_one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# Y - 1
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 1
nx = 1
zy = 0
ny = 0
f  = 1
no = 0

out = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.y_minus_one(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X + Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 0
ny = 0
f  = 1
no = 0

out = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_plus_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X - Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 1
zy = 0
ny = 0
f  = 1
no = 1

out = [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_minus_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# Y - X
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 0
ny = 1
f  = 1
no = 1

out = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.y_minus_x(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X & Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 0
zy = 0
ny = 0
f  = 0
no = 0

out = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_and_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))

# X | Y
x = [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

zx = 0
nx = 1
zy = 0
ny = 1
f  = 0
no = 1

out = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

result = alu.compute(zx, nx, zy, ny, f, no, x, y)
result2 = alu.x_or_y(x,y)
if result != out or result2 != out:
    sys.exit('Error, zx{}, nx{}, zy{}, ny{}, f{}, no{}, x{}, y{} should output {} but got: {}, {}'
       .format(zx, nx, zy, ny, f, no, x, y, out, result, result2))


print("Test for Alu passed successfully.")
