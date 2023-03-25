from simplification import Simplify

class Fraction:
    def __init__(self,numerator,denimenator):
        self.nume = numerator
        self.deno = denimenator

    def __add__(self,other):
        temp_nume = self.nume * other.deno + self.deno * other.nume
        temp_deno = self.deno * other.deno
        s1 = Simplify(temp_nume,temp_deno)
        return s1.simplification()

    def __sub__(self,other):
        temp_nume = self.nume * other.deno - self.deno * other.nume
        temp_deno = self.deno * other.deno
        s1 = Simplify(temp_nume,temp_deno)
        return s1.simplification()

    def __mul__(self,other):
        temp_nume = self.nume * other.nume
        temp_deno = self.deno * other.deno
        s1 = Simplify(temp_nume,temp_deno)
        return s1.simplification()

    def __truediv__(self,other):
        temp_nume = self.nume * other.deno
        temp_deno = self.deno * other.nume
        s1 = Simplify(temp_nume,temp_deno)
        return s1.simplification()

fraction1 = Fraction(5,3)
fraction2 = Fraction(2,4)
print(fraction1+fraction2)
print(fraction1-fraction2)
print(fraction1*fraction2)
print(fraction1/fraction2)