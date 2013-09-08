class BigNatural:
    def __init__(self, int_string='', size=0):
        if int_string:
            self.digits = map(int, list(int_string))
        else:
            self.digits = []
            self.pad(size)

    def __str__(self):
        return ''.join(map(str, self.digits))
        
    def pad(self, width, value=0):
        def pad_rec(xs, n):
            if n <= 0:
                return xs
            else:
                return pad_rec([value] + xs , n - 1)

        self.digits = pad_rec(self.digits, width - len(self.digits))

    def __add__(self, other):
        assert isinstance(other, BigNatural)

        longer_digit_length = max(len(self.digits), len(other.digits))
        self.pad(longer_digit_length)
        other.pad(longer_digit_length)

        def add_rec(addend_pairs, carry, result):
            if addend_pairs == []:
                if carry == 0:
                    return result
                else:
                    return result + [carry]
            else: 
                addends = addend_pairs.pop()
                a1 = addends[0]
                a2 = addends[1]
                lsd = (a1 + a2 + carry) % 10
                carry = (a1 + a2 + carry) / 10

                return add_rec(addend_pairs, carry, result + [lsd])

        digits_of_sum = add_rec(zip(self.digits, other.digits), 0, [])[::-1]
        result = BigNatural(int_string=None, size=len(digits_of_sum))
        result.digits = digits_of_sum
        return result 

    def __iadd__(self, other):
        self.digits = (self + other).digits
        return self

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        longer_digit_length = max(len(self.digits), len(other.digits))
        self.pad(longer_digit_length)
        other.pad(longer_digit_length)

        def eq_rec(digit_pairs):
            if digit_pairs == []:
                return True
            else:
                digits = digit_pairs.pop()

                if digits[0] != digits[1]:
                    return False
                else:
                    return eq_rec(digit_pairs)

        return eq_rec(zip(self.digits, other.digits))

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        product = BigNatural("0")
        n = BigNatural("0")

        while n != other:
            product += self
            n += BigNatural("1")

        return product

    def __imul__(self, other):
        self.digits = (self * other).digits
        return self

    def __pow__(self, other):
        exponentiation = BigNatural("1")
        n = BigNatural("0")

        while n != other:
            exponentiation *= self
            n += BigNatural("1")

        return exponentiation

    __rmul__ = __mul__

