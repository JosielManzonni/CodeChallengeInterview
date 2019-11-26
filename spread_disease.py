"""
The government want know how long will take for a disease spread in the city.
Give a matrix that each cells represent a house and each house with value 1 already is contamined, calc how long it will take

cell with 0 is not infected yet.

rule:
    1- each house only see adjacent neighbor
    2- the disease take 1 day to infect the neighbor's house

ex:

input
------
0 0 1
0 0 1 
0 0 0

output
------
3
      
"""

# globalGrid = [
#                 [0, 0, 0, 1],
#                 [0, 0, 0, 0],
#                 [0, 0, 0, 0],
#                 [0, 0, 0, 0]
#              ]
# globalGrid = [
#                 [0, 1, 1, 0, 1],
#                 [0, 1, 0, 1, 0],
#                 [0, 0, 0, 0, 1],
#                 [0, 1, 0, 0, 0]
#              ]
globalGrid = [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0]
             ]

def print_matrix():
    for i in range(0, len(globalGrid)):
        for j in range(0, len(globalGrid[0])):
            print(globalGrid[i][j], end=' ')
        print()
    print()

def main():
    row = len(globalGrid)
    column = len(globalGrid[0])
    node_queue = []
    many_times_added_in_queue = 0
    for i in range(0,row):
        for j in range(0,column):
            if globalGrid[i][j] == 1:
                #if node is marked add him to queue
                node_queue.append((i,j))

    if len(node_queue) == 0:
        return -1 #no one has the file to share

    while len(node_queue) > 0 :
        add_queue = False
        r, c = node_queue.pop(0) #get first element from the queue --- dequeue
        # print("Get item ({},{}) -> {}".format(r,c,globalGrid[r][c]))
        #up
        if(r>0 and globalGrid[r-1][c]==0 ):
            globalGrid[r-1][c] = globalGrid[r][c] + 1
            # print("\titem ({},{}) -> {}".format(r-1, c, globalGrid[r-1][c]))
            node_queue.append( (r-1,c) )
            add_queue = True
        #down
        if(r < row-1 and globalGrid[r+1][c]==0 ):
            globalGrid[r+1][c] = globalGrid[r][c] + 1
            # print("\titem ({},{}) -> {}".format(r+1, c, globalGrid[r+1][c]))
            node_queue.append((r+1, c))
            add_queue = True
        #left
        if(c > 0 and globalGrid[r][c-1] == 0):
            globalGrid[r][c-1] = globalGrid[r][c] + 1
            # print("\titem ({},{}) -> {}".format(r, c-1, globalGrid[r][c-1]))
            node_queue.append((r, c-1))
            add_queue = True

        #right
        if(c < column-1 and globalGrid[r][c+1] == 0):
            globalGrid[r][c+1] = globalGrid[r][c] + 1
            # print("\titem ({},{}) -> {}".format(r, c+1, globalGrid[r][c+1]))
            node_queue.append((r, c+1))
            add_queue = True
        
        print_matrix()
        
        if add_queue:
            many_times_added_in_queue = globalGrid[r][c] + 1 
    print('It will take {} days to spread the disease'.format(many_times_added_in_queue-1))

main()
