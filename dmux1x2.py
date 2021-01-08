

class DMux1x2:
    def compute(self, sel, a):
        if sel == 0:
            return a, 0
        else:
            return 0, a
