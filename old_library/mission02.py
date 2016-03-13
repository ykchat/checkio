from math import sqrt

def isPalindrome(number):

    s = str(number)

    return s == s[::-1]

def isPrime(number):

    max = int(sqrt(number))+1

    divs = list(range(max))

    divs[0] = 0
    divs[1] = 0

    for div in divs:
        if div == 0:
            continue
        if number % div == 0:
            return False
        for multi in range(div+div, max, div):
            divs[multi] = 0

    return True


def checkio(number):

    if isPalindrome(number) and isPrime(number):
        return number
    else:
        return checkio(number+1)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'
    assert checkio(115) == 131, 'Fourth example'
