def checkio(data):

    data = data.lower()

    chars = [x for x in set(data) if x.isalpha()]
    chars.sort()

    result = ''

    max = 0
    for char in chars:
        count = data.count(char)
        if count > max:
            max = count
            result = char

    return result

if __name__ == '__main__':

    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
