import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from and2way1bit import And2Way1Bit
from not1way1bit import Not1Way1Bit
from or16way1bit import Or16Way1Bit
from or2way1bit import Or2Way1Bit
from mux8way1bit import Mux8Way1Bit


class JumpDecoder:

    def compute(self, alu_out, j1, j2, j3):
        not_sign_bit = Not1Way1Bit()

        sign_bit = alu_out[0]
        is_positive = not_sign_bit.compute(sign_bit)
        is_negative = sign_bit

        or16way1bit = Or16Way1Bit()
        alu_or_out = or16way1bit.compute(alu_out)

        and_gt = And2Way1Bit()
        and_eq = And2Way1Bit()
        not_eq = Not1Way1Bit()
        not_ge = Not1Way1Bit()
        or_ge = Or2Way1Bit()
        or_ne = Or2Way1Bit()
        not_le = Not1Way1Bit()
        and_le = And2Way1Bit()
        or_le = Or2Way1Bit()

        null = 0
        gt = and_gt.compute(is_positive, alu_or_out)
        eq = and_eq.compute(is_positive, not_eq.compute(alu_or_out))
        ge = or_ge.compute(is_positive, not_ge.compute(alu_or_out))
        lt = is_negative
        ne = or_ne.compute(gt, lt)
        le = or_le.compute(is_negative, and_le.compute(not_le.compute(alu_or_out), is_positive))
        jmp = 1

        mux = Mux8Way1Bit()
        return mux.compute([j1, j2, j3], null, gt, eq, ge, lt, ne, le, jmp)
