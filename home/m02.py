def checkio(data):

    data.sort()

    median = 0
    c = len(data)//2

    if len(data) % 2 == 1:
        median = data[c]
    else:
        median = (data[c-1]+data[c])/2.0

    return median

if __name__ == '__main__':

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
