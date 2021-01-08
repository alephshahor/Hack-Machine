from mux2way1bit import Mux2Way1Bit

class Mux2Way16Bit:

    def compute(self, sel, a, b):

        assert len(a) == 16
        assert len(b) == 16

        mux2Way1Bit = Mux2Way1Bit()
        return mux2Way1Bit.compute(sel, a, b)
