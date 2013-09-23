from sys import argv
import re 
MIN_VAL = 1
MAX_VAL = 1000

some_special_numbers_in_english = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    15 : "fifteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty"
}

NUMBER_RE = re.compile(r"(?:^.*?)(?P<Thousands>\d{0,3}?)((?P<Hundreds>\d{1,3})$)")
HYPHENS_OR_SPACES_RE = re.compile(r"[-\s]")

def number_to_english(n):
    matches = NUMBER_RE.match(str(n))
    thousands_digits = matches.group("Thousands")
    hundreds_digits = matches.group("Hundreds")
    english = ''

    if thousands_digits:
        english += three_digits_to_english(thousands_digits) + " thousand"

        if int(hundreds_digits) > 0:
            english += " and "

    english += three_digits_to_english(hundreds_digits)
    return english

def three_digits_to_english(n):
    digits = str(n)
    assert 0 <= len(digits) <= 3
    
    if len(digits) < 3:
        digits = ''.join((['0'] * (3 - len(digits)) + list(digits)))
 
    tens = digits[1]
    ones = digits[2]
    tens_and_ones = int(tens + ones)
    hundreds = int(digits[0])
    english = ''

    if hundreds is not 0:
        english += some_special_numbers_in_english[hundreds] + " hundred"

        if tens_and_ones == 0:
            return english
        else:
            english += " and "

    if tens_and_ones in some_special_numbers_in_english and tens_and_ones != 0:
        english += some_special_numbers_in_english[tens_and_ones]
    else:
        if tens == "0":
            if ones != "0":
                english += some_special_numbers_in_english[int(ones)]
        elif tens == "1":
            english += some_special_numbers_in_english[int(ones)] + "teen"
        elif tens in map(str, range(6,10)):
            english += some_special_numbers_in_english[int(tens)] + "ty-" +\
                       some_special_numbers_in_english[int(ones)]
        else:
            tens += "0" 
            english += some_special_numbers_in_english[int(tens)] + "-" +\
                       some_special_numbers_in_english[int(ones)]

    return english.replace("eightt", "eight")

if __name__ == "__main__":
    print ("currently handles only numbers in range [%d, %d]" % (MIN_VAL, MAX_VAL))

    letter_count = 0

    for i in range(MIN_VAL, MAX_VAL + 1):
        english = number_to_english(i)
        letter_count += len(english)

        number_of_hyphens_and_spaces = len(HYPHENS_OR_SPACES_RE.findall(english))

        if number_of_hyphens_and_spaces:
            letter_count -= len(HYPHENS_OR_SPACES_RE.findall(english))

    print letter_count

