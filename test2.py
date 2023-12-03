class Fraction:
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def mul(self, f2):
       # result = (self.s * f2.s) / (self.m * f2.m)        
       result_s = self.s * f2.s
       result_m = self.m * f2.m
       result = Fraction(result_s, result_m)
       return result

    def sum(self, f2):
        result_s = (self.s * f2.m) + (f2.m * self.m)
        result_m =  self.m * f2.m
        result = Fraction(result_s, result_m)
        return result

    def sub (self, f2):
        # resultsub = a/b - c/d = (ad - bc) / bd
        result_ssub = (self.s * f2.m) - (f2.s * self.m)
        result_msub = self.m * f2.m
        resultsub = Fraction(result_ssub, result_msub)
        return resultsub

    def div(self):
        # resultdiv = (a/b) / (c/d) = ad/bc
        result_sdiv = self.s * f2.m
        result_mdiv = self.m * f2.s
        resultdiv = Fraction(result_sdiv, result_mdiv)
        return resultdiv
        

    def show(self):
        print(self.s, "/", self.m)

f1 = Fraction(2, 3)   
f1.show()

f2 = Fraction(4, 5)
f2.show()

# result_m = Fraction.mul(f1, f2)
result_mul = f1.mul(f2)
# print(result_m)
result_mul.show()

result_sum = f1.sum(f2)
result_sum.show()
