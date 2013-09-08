from bignatural import BigNatural

result_as_string = str(BigNatural("2") ** BigNatural("1000"))

result_as_int_list = map(int, ''.join(result_as_string))

sum_of_digits = sum(result_as_int_list)
print sum_of_digits
