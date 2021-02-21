
class Mux2Way1Bit:

    def compute(self, sel, a, b):

        if sel == 0:
            return a
        if sel == 1:
            return b
