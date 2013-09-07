import heapq

def input_length_range_of_n_digit_multiplicands(n):
    product_for_max_multiplicands_input_length = n*2
    product_for_min_multiplicands_input_length = \
            product_for_max_multiplicands_input_length - 1

    return (product_for_max_multiplicands_input_length, \
            product_for_min_multiplicands_input_length)

def chars_to_int(char_list):
    return int(''.join(char_list))

def int_to_chars(x):
    return list(str(x))

def n_digit_num_max_val(n):
    max_value_string_list = ['9'] * n
    return chars_to_int(max_value_string_list)

def n_digit_num_min_val(n):
    min_value_string_list = ['0'] * n
    min_value_string_list[0] = '1'
    return chars_to_int(min_value_string_list)

def palindromes_of_size(n):
    if n <= 0:
        raise ValueError("n must be at least 1")

    is_odd = lambda: n % 2 is 1

    num_digits_for_left_half = n/2
    max_value_for_left_half = n_digit_num_max_val(num_digits_for_left_half)

    if is_odd():
        max_value_for_left_half *= 10
        max_value_for_left_half += 9

    input_length_of_left_half = len(int_to_chars(max_value_for_left_half))
    min_value_for_left_half = n_digit_num_min_val(input_length_of_left_half)

    for left_half in range(max_value_for_left_half,\
                           min_value_for_left_half - 1, -1):
	left_half_as_string_list = int_to_chars(left_half)
	right_half_as_string_list = left_half_as_string_list[::-1]

	if is_odd():
	    right_half_as_string_list.pop(0)

	palindrome = \
	    chars_to_int(left_half_as_string_list + right_half_as_string_list)

	yield palindrome

	    
def is_divisible_by_two_n_digit_number(x, n):
    max_divisor = n_digit_num_max_val(n)
    min_divisor = n_digit_num_min_val(n)

    for divisor in range(max_divisor, min_divisor, -1):
        if x % divisor is 0:
            if len(int_to_chars(x / divisor)) is n:
	        return True

    return False

def max_palindrome_product_of_two_two_n_digit_multiplicands(n):
    min_size, max_size = sorted(input_length_range_of_n_digit_multiplicands(n))

    for x in palindromes_of_size(max_size):
        if is_divisible_by_two_n_digit_number(x, n):
	    return x
        
print max_palindrome_product_of_two_two_n_digit_multiplicands(3)
