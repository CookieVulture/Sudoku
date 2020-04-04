game = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def game_print(screen):
    for row in range(len(screen)):
        if row % 3 == 0 and row!=0:
            print("- - - - - - - - - - - - -")

        for column in range(len(screen[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end="")

            if column == 8:
                print(screen[row][column])
            else:
                print(str(screen[row][column])+" ", end="")


def find_zero(screen):
    for row in range(len(screen)):
        for column in range(len(screen[0])):
            if screen[row][column] == 0:
                return row, column
    return None


def isvalid(screen, number, position):

    # Row
    for column in range(len(screen[0])):
        if screen[position[0]][column] == number and position[1] != column:
            return False

    # Column
    for column in range(len(screen[0])):
        if screen[column][position[1]] == number and position[0] != column:
            return False

    # Box
    box_a = position[1] // 3
    box_b = position[0] // 3
    for i in range (box_b*3, box_b*3+3):
        for j in range (box_a*3, box_a*3+3):
            if screen[i][j] == number and (i, j) != position:
                return False

    return True


def backtracking(screen):

    find = find_zero(screen)
    if not find:
        return True
    else:
        row, column = find

    for num in range(1,10):
        if isvalid(screen, num, (row, column)):
            screen[row][column] = num

            if backtracking(screen):
                return True

            screen[row][column] = 0
    return False


game_print(game)
backtracking(game)
print()
game_print(game)
