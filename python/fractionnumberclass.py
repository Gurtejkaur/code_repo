class Rational:
    def __init__(self,num,den):
        self.numerator = num
        if den!=0:
            self.denominator=den
        else:
            raise ValueError("attempt to make an illegal rational number")
                
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def set_numerator(self,n):
        self.numerator=n
        
    def set_denominator(self,d):
        if d!=0:
            self.denominator=d
        else:
            raise ValueError("attempt to make an illegal rational number")
                
    def __mul__(self,other):
        return Rational(self.numerator*other.numerator,self.denominator*other.denominator)
    
    def __add__(self,other):
        pass
    def __str__(self):
        return str(self.get_numerator())+'/'+ str(self.get_denominator())
def main():
    fract1=Rational(1,2)
    fract2=Rational(2,3)
    print("fract1=",fract1)
    print("fract2=",fract2)
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(1)
    fract2.set_denominator(10)
    print("fract1=",fract1)
    print("fract2=",fract2)
    fract3=Rational(1,2)
    fract4=Rational(3,5)
    print(fract3,'*',fract4,"=",fract3*fract4)
    #fract5=Rational(4,0)
    
    print(fract3.__mul__(fract4))
    print(fract4.__str__())
main()    
    
    
    
    
