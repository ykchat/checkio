symbols = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 5000:'.'}
bases = [[1000, 5000, 10000], [100, 500, 1000], [10, 50, 100], [1, 5, 10]]

def checkio(data):

    result = '';

    for basis in bases:
        digit = data // basis[0]
        if digit == 9:
            result += symbols[basis[0]]
            result += symbols[basis[2]]
        elif digit > 4:
            result += symbols[basis[1]]
            result += symbols[basis[0]] * (digit-5)
        elif digit == 4:
            result += symbols[basis[0]]
            result += symbols[basis[1]]
        elif digit > 0:
            result += symbols[basis[0]] * digit
        data = data % basis[0] 

    return result

if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
