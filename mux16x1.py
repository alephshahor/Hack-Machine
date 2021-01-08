from mux2x1 import Mux2x1

class Mux16x1:

    def compute(self,sel,in_):
        decimal_sel = ''.join(str(e) for e in sel)
        decimal_sel = int(decimal_sel, 2)
        return in_[decimal_sel]
