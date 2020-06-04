from create import make_grid

grid = make_grid()


def search_in_row():
    for c in range(3):
        for d in range(3):
            if grid[c][y][z][d] == 0 and (c != i and d != a):
                print(1)

def search_in_col():
    for e in range(3):
        for f in range(3):
            if grid[i][e][f][a] == 0 and (e != y and f != z):
                print(1)


for i in range(3):
    for y in range(3):
        for z in range(3):
            for a in range(3):
                if grid[i][y][z][a] == 0:
                    search_in_row()
                    search_in_col()
                    break


print(grid)