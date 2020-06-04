import numpy as np
from random import randint

grid = np.zeros((3, 3, 3, 3), dtype='Int32')

def check_possibility(num, x, y, j, k):
    result = True
    # ha üres az a hely
    if grid[x][y][j][k] == 0:
        # kockában van e olyan
        for a in range(3):
            for b in range(3):
                if grid[x][y][a][b] == num:
                    result = False
                    break

        # sorában van-e ugyan olyan
        for c in range(3):
            for d in range(3):
                if grid[c][y][j][d] == num:
                    result = False
                    break

        # oszlopában van-e ugyan olyan
        for e in range(3):
            for f in range(3):
                if grid[x][e][f][k] == num:
                    result = False
                    break

    else:
        result = False

    return result


def make_grid():
    # random megadja, hogy hány számot ír be alapból
    for i in range(randint(17, 50)):
        num = randint(1, 9)
        x = randint(0, 2)
        y = randint(0, 2)
        j = randint(0, 2)
        k = randint(0, 2)

        if check_possibility(num, x, y, j, k) == True:
            grid[x][y][j][k] = num

    return grid