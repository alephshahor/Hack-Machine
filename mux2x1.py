

class Mux2x1: 
    def compute(self, sel, a, b):
        if sel == 0:
            return a
        if sel == 1:
            return b
