"""
Give a matrix that each cells can represent a lake or mountain. Count how many lakes has in the matrix

cell with 1 represent lake
cell with 0 represent mountain

rule:
    1- if adjacent cells has lake this count as only one.


input
------

1 0 1
0 0 1
1 1 0

output
------

3

"""

# globalGrid = [
#     [1, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0],
#     [1, 0, 1, 1],
#     [1, 1, 1, 1]
# ]

# globalGrid = [
#     [1, 1, 0, 0],
#     [0, 1, 1, 0],
#     [0, 0, 0, 0],
#     [1, 0, 1, 1],
#     [1, 1, 1, 1]
# ]
globalGrid = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]



def countPlace(r, c):
    # print("\t[{}][{}]".format(r, c))
    #up
    globalGrid[r][c] = -1
    if (r-1) >= 0:
        if globalGrid[r-1][c] > 0:
            print("\tup")
            countPlace(r-1, c)
    #down
    if (r+1) < len(globalGrid):
        if globalGrid[r+1][c] > 0:
            print("\tdown")
            # globalGrid[r][c] = -1
            countPlace(r+1, c)
    #left
    if (c-1) >= 0:
        if globalGrid[r][c-1] > 0:
            print("\tleft")
            # globalGrid[r][c] = -1
            countPlace(r, c-1)
    #right
    if (c+1) < len(globalGrid[0]):
        if globalGrid[r][c+1] > 0:
            print("\tright")
            # globalGrid[r][c] = -1
            countPlace(r, c+1)
    return


def main():
    row = len(globalGrid)
    column = len(globalGrid[0])
    count = 0
    for r in range(0, row):
        for c in range(0, column):
            if(globalGrid[r][c] == 1):
                print("Root [{}][{}]".format(r,c))
                count +=1
                countPlace(r, c)

    print(count)


main()
