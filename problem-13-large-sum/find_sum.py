numbers = []

with open ('numbers_file', 'r') as f:
    for number_as_string in f:
        number_as_char_list = list(number_as_string.rstrip('\n'))
        number_as_int_list = map(int, number_as_char_list)
        numbers.append(number_as_int_list)

summation = []
addends = []
carry = 0

for digit in range(len(numbers[0])):
    for number in numbers:
        addends.append(number.pop())

    radix_sum = carry + sum(addends)
    least_significant_digit = radix_sum % 10
    carry = radix_sum / 10
    summation.append(least_significant_digit)

leftover = carry
summation.extend([int(d) for d in list(str(leftover))][::-1])
summation.reverse()

print summation[:10]
