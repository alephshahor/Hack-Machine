from or2x1 import Or2x1

class Or16x1:
    
    def compute(self, in_):
        or2x1 = Or2x1()
        result = in_[0]

        for i in range(len(in_)-1):
            result = or2x1.compute(result, in_[i+1])
        return result
            
