from and2x1 import And2x1

class And16x1:
    def compute(self, in_):
        and2x1 = And2x1()
        result = in_[0]
        for i in range(len(in_) - 1):
            result = and2x1.compute(result, in_[i+1])
        return result
            
