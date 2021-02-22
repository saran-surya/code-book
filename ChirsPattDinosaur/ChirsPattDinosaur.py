def findPaths(matrix, x, y, visited=[[]], right=True, down=True):
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
    if right and findPaths(matrix, x, y+1, visited):
        temp = ''.join(visited[-1])
        finalResult.append(temp)
        visited.append([])
    elif visited[-1] != [] and visited[-1][-1] == "R":
        visited[-1].pop()
    visited[-1].append("D")
    if down and findPaths(matrix, x+1, y, visited):
        temp = ''.join(visited[-1])
        finalResult.append(temp)
        visited.append([])
    elif visited[-1] != [] and visited[-1][-1] == "D":
        visited[-1].pop()


r = int(input())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))
finalResult = []
findPaths(matrix, 0, 0)
finalResult = finalResult[::-1]
initial = finalResult[-1]
for i in range(len(finalResult)):
    temp = initial[:abs(len(finalResult[i])-len(initial))]
    if(temp == ''):
        initial = finalResult[i]
    temp += finalResult[i]
    print(temp + "R")