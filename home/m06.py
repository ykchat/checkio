FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    result = ''

    digit = number // 100
    if digit > 0:
        result += FIRST_TEN[digit-1]
        result += ' '
        result += HUNDRED
        result += ' '
        number = number % 100

    digit = number // 10
    if digit > 1:
        result += OTHER_TENS[digit-2]
        result += ' '
        number = number % 10
    elif digit == 1:
        digit = number % 10
        result += SECOND_TEN[digit]
        result += ' '
        number = 0

    digit = number
    if digit > 0:
        result += FIRST_TEN[digit-1]

    result = result.rstrip();

    return result

if __name__ == '__main__':

    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
