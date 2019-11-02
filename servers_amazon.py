globalGrid = [
                [0, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
             ]
# globalGrid = [
#                 [0, 1, 1, 0, 1],
#                 [0, 1, 0, 1, 0],
#                 [0, 0, 0, 0, 1],
#                 [0, 1, 0, 0, 0]
#              ]
# globalGrid = [
#                 [0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0],
#                 [0, 1, 0, 0, 0, 0]
#              ]

def calcDist( r, c, dist):
    #up
    if (r-1) >= 0:
        if globalGrid[r-1][c] != 1:
            if globalGrid[r-1][c] == 0 or globalGrid[r-1][c] > dist:
                globalGrid[r-1][c] = dist
                calcDist(r-1,c, dist+1)
    #down
    if (r+1) < len(globalGrid):
        if globalGrid[r+1][c] != 1:
            if globalGrid[r+1][c] == 0 or globalGrid[r+1][c] > dist:
                globalGrid[r+1][c] = dist
                calcDist(r+1,c, dist+1)
    #left
    if (c-1) >= 0:
        if globalGrid[r][c-1] != 1:
            if globalGrid[r][c-1] == 0 or globalGrid[r][c-1] > dist:
                globalGrid[r][c-1] = dist
                calcDist(r,c-1, dist+1)
    #right
    if (c+1) < len(globalGrid[0]):
        if globalGrid[r][c+1] != 1:
            if globalGrid[r][c+1] == 0 or globalGrid[r][c+1] > dist:
                globalGrid[r][c+1] = dist
                calcDist(r,c+1, dist+1)
    return


def main():
    row = len(globalGrid)
    column = len(globalGrid[0])
    for r in range(0, row):
        for c in range(0, column):
            if( globalGrid[r][c] == 1):
                # globalGrid[r][c] = -1 #mark as incomum
                print("Global [{}][{}] = {}".format(r, c, globalGrid[r][c]))
                calcDist(r,c,2)
    # print(globalGrid)
    mini = globalGrid[0][0]
    for r in range(0, row):
        for c in range(0, column):
            if globalGrid[r][c] >1 and mini < globalGrid[r][c]:
                mini = globalGrid[r][c]
    print(mini-1)

main()
