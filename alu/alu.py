import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux2way16bit import Mux2Way16Bit
from not1way16bit import Not1Way16Bit

sys.path.append(os.environ['ROOT_FOLDER'] + '/memory')
from add16bit import Add16Bit

from and2way16bit import And2Way16Bit


class Alu:


    def zero(self, x, y):

        zx = 1
        nx = 0
        zy = 1
        ny = 0
        f  = 1
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)


    def one(self, x, y):

        zx = 1
        nx = 1
        zy = 1
        ny = 1
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def minus_one(self, x, y):

        zx = 1
        nx = 1
        zy = 1
        ny = 0
        f  = 1
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def x(self, x, y):

        zx = 0
        nx = 0
        zy = 1
        ny = 1
        f  = 0
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def not_x(self, x, y):

        zx = 0
        nx = 0
        zy = 1
        ny = 1
        f  = 0
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def minus_x(self, x, y):

        zx = 0
        nx = 0
        zy = 1
        ny = 1
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def y(self, x, y):

        zx = 1
        nx = 1
        zy = 0
        ny = 0
        f  = 0
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)


    def not_y(self, x, y):

        zx = 1
        nx = 1
        zy = 0
        ny = 0
        f  = 0
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def minus_y(self, x, y):

        zx = 1
        nx = 1
        zy = 0
        ny = 0
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)


    def x_plus_one(self, x, y):

        zx = 0
        nx = 1
        zy = 1
        ny = 1
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def y_plus_one(self, x, y):

        zx = 1
        nx = 1
        zy = 0
        ny = 1
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def x_minus_one(self, x, y):

        zx = 0
        nx = 0
        zy = 1
        ny = 1
        f  = 1
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def y_minus_one(self, x, y):

        zx = 1
        nx = 1
        zy = 0
        ny = 0
        f  = 1
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def x_plus_y(self, x, y):

        zx = 0
        nx = 0
        zy = 0
        ny = 0
        f  = 1
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)


    def x_minus_y(self, x, y):

        zx = 0
        nx = 1
        zy = 0
        ny = 0
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def y_minus_x(self, x, y):

        zx = 0
        nx = 0
        zy = 0
        ny = 1
        f  = 1
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def x_and_y(self, x, y):

        zx = 0
        nx = 0
        zy = 0
        ny = 0
        f  = 0
        no = 0

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def x_or_y(self, x, y):

        zx = 0
        nx = 1
        zy = 0
        ny = 1
        f  = 0
        no = 1

        return self.compute(zx, nx, zy, ny, f, no, x, y)

    def compute(self, zx, nx, zy, ny, f, no, x, y):

        zero_16 = [0] * 16

        not1Way16Bit = Not1Way16Bit()
        add16Bit = Add16Bit()
        and2Way16Bit = And2Way16Bit()

        zx_mux = Mux2Way16Bit()
        nx_mux = Mux2Way16Bit()

        zy_mux = Mux2Way16Bit()
        ny_mux = Mux2Way16Bit()

        f_mux = Mux2Way16Bit()

        no_mux = Mux2Way16Bit()

        zx_out = zx_mux.compute(zx, x, zero_16)
        not_zx_out  = not1Way16Bit.compute(zx_out)
        nx_out = nx_mux.compute(nx, zx_out, not_zx_out)

        zy_out = zy_mux.compute(zy, y, zero_16)
        not_zy_out  = not1Way16Bit.compute(zy_out)
        ny_out = ny_mux.compute(ny, zy_out, not_zy_out)

        nx_out_add_ny_out = add16Bit.compute(nx_out, ny_out)
        nx_out_and_ny_out = and2Way16Bit.compute(nx_out, ny_out)

        f_out = f_mux.compute(f, nx_out_and_ny_out, nx_out_add_ny_out)
        not_f_out = not1Way16Bit.compute(f_out)

        no_out = no_mux.compute(no, f_out, not_f_out)
        return no_out
