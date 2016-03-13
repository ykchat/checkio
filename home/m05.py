def checkio(number):

    mins = 0
    pigs = 0

    while number >= 0:
        mins += 1
        pigs += mins
        number -= pigs

    return max([pigs-mins, pigs+number])

if __name__ == '__main__':

    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
