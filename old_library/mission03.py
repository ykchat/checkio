from itertools import combinations

def checkio(data):

    count = 0

    for sides in combinations(data, 3):
        sides = sorted(sides)
        if sides[0] + sides[1] < sides[2]:
            count += 1

    return count

if __name__ == '__main__':

    assert checkio([4, 2, 10]) == 1, "First"
    assert checkio([1, 2, 3]) == 0, "Second"
    assert checkio([5, 2, 9, 6]) == 2, "Third"
