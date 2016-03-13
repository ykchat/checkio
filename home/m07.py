def checkio(game_result):

    result = 'D'

    game_result.append(game_result[0][0] + game_result[1][0] + game_result[2][0])
    game_result.append(game_result[0][1] + game_result[1][1] + game_result[2][1])
    game_result.append(game_result[0][2] + game_result[1][2] + game_result[2][2])
    game_result.append(game_result[0][0] + game_result[1][1] + game_result[2][2])
    game_result.append(game_result[0][2] + game_result[1][1] + game_result[2][0])

    for line in game_result:
        line = set(line)
        if len(line) == 1:
            char = line.pop()
            if char != '.':
                result = char
                break

    return result

if __name__ == '__main__':

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
