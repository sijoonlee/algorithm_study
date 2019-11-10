import math

class Karatsuba(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a
    def set_b(self, b):
        self.b = b
    def test(self):
        print( self.a * self.b )
    
    def len(self, n):
        if n == 0:
            len = 1
        else:
            len = int(math.log10(n))+1
        return len

    def add_zero(self, a, b):
        how_many_zeros = 0

        len_a = self.len(a)
        len_b = self.len(b)

        if len_a > len_b:
            diff = len_a - len_b
            how_many_zeros = how_many_zeros + diff
            b = b * (10**diff)
        elif len_a < len_b:
            diff = len_b - len_a
            how_many_zeros = how_many_zeros + diff
            a = a * (10**diff)

        len_a = self.len(a)
        len_b = self.len(b)
        if len_a != 1 and len_a % 2 != 0:
            a = a * 10
            b = b * 10
            how_many_zeros = how_many_zeros + 2
    
        return a, b, how_many_zeros
    
    def divide(self, n):
        if n == 0:
            digits = 1
        else:
            digits = int(math.log10(n))+1

        digits = digits / 2
        n_left = int( n / (10**digits) )
        n_right = int(n - n_left * (10**digits))

        return n_left, n_right

    def mul(self, a, b):
        a,b,how_many_zeros = self.add_zero(a,b)

        if a == 0:
            digits = 1
        else:
            digits = int(math.log10(a))+1

        #print(digits)
        if digits == 1:
            return a*b
        else:
            a_left, a_right = self.divide(a)
            b_left, b_right = self.divide(b)
            x1 = self.mul(a_left, b_left)
            x2 = self.mul(a_right, b_right)
            x3 = self.mul(a_left + a_right, b_left + b_right)
            result = (10**digits) * x1 + (10**(digits/2)) * ( x3 - x2 - x1 ) + x2
            return int( result / (10 ** how_many_zeros) )

    def run(self):
        print( self.mul(self.a, self.b) )



if __name__ == "__main__":


    a = 1
    b = 100
    calculator = Karatsuba(a,b)
    calculator.run()
    calculator.test()

    a = 22
    b = 334
    calculator = Karatsuba(a,b)
    calculator.run()
    calculator.test()

    a = 100000001
    b = 100000001
    calculator = Karatsuba(a,b)
    calculator.run()
    calculator.test()

    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    calculator = Karatsuba(a,b)
    calculator.run()
    calculator.test()

# 100
# 100
# 7348
# 7348
# 10000000200000002 --> Bug!?
# 10000000200000001
# 8539734222673565727722948056719317944556312698501627377409191379033726264982769845827675624200334881483773142083314390902243328
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184