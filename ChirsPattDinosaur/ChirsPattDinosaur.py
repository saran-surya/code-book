def movement(matrix, x, y, visited=[[]], right=True, down=True):
    visited = visited
    if(x == len(matrix)-1 and y == len(matrix[0])-1 and matrix[x][y] == 1):
        return True
    if(matrix[x][y] == 0):
        return False
    if(y == len(matrix[0])-1) and right:
        right = False
    if x == len(matrix)-1 and down:
        down = False
    visited[-1].append("R")
    if right and movement(matrix, x, y+1, visited):
        temp = ''.join(visited[-1])
        tally.append(temp)
        visited.append([])
    elif visited[-1] != [] and visited[-1][-1] == "R":
        visited[-1].pop()
    visited[-1].append("D")
    if down and movement(matrix, x+1, y, visited):
        temp = ''.join(visited[-1])
        tally.append(temp)
        visited.append([])
    elif visited[-1] != [] and visited[-1][-1] == "D":
        visited[-1].pop()
    # if(x == 0 and y == 0):
    #     return visited


r = int(input())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

# matrix = [[1, 1, 1, 1],
#           [1, 1, 1, 1],
#           [1, 1, 1, 1]]

# matrix = [[1, 0, 0, 0],
#           [1, 1, 0, 1], 
#           [1, 1, 0, 0], 
#           [0, 1, 1, 1]]

tally = []
movement(matrix, 0, 0)

initial = tally[0]
for i in range(len(tally)):
    if tally[i] == initial:
        print(tally[i] + "R")
    else:
        temp = initial[:abs(len(tally[i])-len(tally[0]))]
        if(temp == ''):
            initial = tally[i]
        temp += tally[i]
        print(temp + "R")

