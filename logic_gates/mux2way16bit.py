from mux2way1bit import Mux2Way1Bit

class Mux2Way16Bit:

    def compute(self, sel, a, b):
        mux2Way1Bit = Mux2Way1Bit()
        return mux2Way1Bit.compute(sel, a, b)
