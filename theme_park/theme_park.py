
# '''
# 4 4
# 1 1 2 1 3 1 1 3
# G G G G
# G W W M
# G G W W
# M G M M
# '''

def totalGrass(matrix, r):
    grass = 0
    for i in range(r):
        grass += matrix[i].count('G')
    return grass


def isHumanValid(matrix, x, y):
    return matrix[x][y] == "G" and (x, y) != GBL_CAGE

def isDinoValid(matrix, x, y):
    return matrix[x][y] == 'G' or matrix[x][y] == 'M'

def isGrassLand(matrix, x, y):
    return matrix[x][y] == 'G'

def dinoMovement(matrix, x, y, visited, top=True, right=True, down=True, left=True, steps=0):
    initialFlags = {"top":top, "right":right, "down":down, "left":left}
    # if((x, y) in GBL_GATES):
    if((x, y) == GBL_FLAG):
        # print("Dino Reached gate in", steps, "steps")
        return steps
    if ((x, y) in visited):
        return False
    visited.append((x, y))
    if x == 0 and top:
        # print("Top movement restricted")
        top = False
    if y == len(matrix[0])-1 and right:
        # print("Right movement restricted")
        right = False
    if y == 0 and left:
        # print("Left movement restricted")
        left = False
    if x == len(matrix)-1 and down:
        # print("Down Movement restricted")
        down = False
    
    if top and isDinoValid(matrix, x-1, y) and dinoMovement(matrix, x-1, y, visited, down=False, steps=steps+1) :
        # print("Top is valid move")
        return dinoMovement(matrix, x-1, y, [], down=False, steps=steps+1)
    elif right and isDinoValid(matrix, x, y+1) and dinoMovement(matrix, x, y+1, visited, left=False, steps=steps+1) :
        # print("Right is a valid move")
        return dinoMovement(matrix, x, y+1, [], left=False, steps=steps+1)
    elif down and isDinoValid(matrix, x+1, y) and dinoMovement(matrix, x+1, y, visited, top=False, steps=steps+1) :
        # print("Down is a valid move")
        return dinoMovement(matrix, x+1, y, [], top=False, steps=steps+1)
    elif left and isDinoValid(matrix, x, y-1) and dinoMovement(matrix, x, y-1, visited, right=False, steps=steps+1) :
        # print("Left is a valid move")
        return dinoMovement(matrix, x, y-1, [], right=False, steps=steps+1)
    else:
        return False

def humanMovement(matrix, x, y, top=True, right=True, down=True, left=True, steps=0):
    initialFlags = {"top":top, "right":right, "down":down, "left":left}
    # print(initialFlags)
    if((x, y) in GBL_GATES):
        # print("Reached gate in", steps, "steps")
        return [steps, (x, y)]
    if ((x, y) == GBL_CAGE):
        return [False]
    if x == 0 and top:
        # print("Top movement restricted")
        top = False
    if y == len(matrix[0])-1 and right:
        # print("Right movement restricted")
        right = False
    if y == 0 and left:
        # print("Left movement restricted")
        left = False
    if x == len(matrix)-1 and down:
        # print("Down Movement restricted")
        down = False
    
    if top and isHumanValid(matrix, x-1, y) and humanMovement(matrix, x-1, y, down=False, steps=steps+1)[0]:
        # print("Top is valid move")
        return humanMovement(matrix, x-1, y, down=False, steps=steps+1)
    elif right and isHumanValid(matrix, x, y+1) and humanMovement(matrix, x, y+1, left=False, steps=steps+1)[0]:
        # print("Right is a valid move")
        return humanMovement(matrix, x, y+1, left=False, steps=steps+1)
    elif down and isHumanValid(matrix, x+1, y) and humanMovement(matrix, x+1, y, top=False, steps=steps+1)[0]:
        # print("Down is a valid move")
        return humanMovement(matrix, x+1, y, top=False, steps=steps+1)
    elif left and isHumanValid(matrix, x, y-1) and humanMovement(matrix, x, y-1, right=False, steps=steps+1)[0]:
        # print("Left is a valid move")
        return humanMovement(matrix, x, y-1, right=False, steps=steps+1)
    else:
        return [False]



# r, c = map(int, input().split())
# r = 4
# c = 4
# # l1 = [1, 1, 2, 1, 3, 1, 1, 3] #ref
# l1 = [1, 1, 2, 1, 3, 1, 1, 3]
# matrix = [['G', 'G', 'G', 'G'], ['G', 'W', 'W', 'M'], ['G', 'G', 'W', 'W'], ['M', 'G', 'M', 'M']]
# r = 4 
# c = 6
# l1 = [1, 6, 3, 6, 4, 6, 3, 4]
r, c = map(int, input().split())
l1 = list(map(int, input().split()))
l1 = [i-1 for i in l1]
matrix = []
for i in range(r):
    matrix.append(list(map(str, input().split())))
GBL_GATES = [(l1[0], l1[1]), (l1[2], l1[3]), (l1[4], l1[5])]
GBL_CAGE  = (l1[-2], l1[-1])
GBL_FLAG = ()
total_safe = 0
unsafe = 0
# matrix = [['W', 'M', 'G', 'G', 'G', 'G'],['M', 'G', 'W', 'G', 'M', 'M'],['G', 'W', 'G', 'G', 'G', 'G'],['W', 'G', 'W', 'M', 'W', 'G']]

for i in range(r):
    for j in range(c):
        if isHumanValid(matrix, i, j):
            human_steps = humanMovement(matrix, i, j)
            if human_steps[-1] != False:
                GBL_FLAG = human_steps[-1]
            else:
                GBL_FLAG = (i, j)
            dino_steps = dinoMovement(matrix, GBL_CAGE[0], GBL_CAGE[-1], [])
            if (not human_steps[-1] and not dino_steps) or (dino_steps > human_steps[0] and human_steps[-1] != False):
                total_safe += 1
                # print("Human ->", human_steps[0])
                # print("Dino->", dino_steps)

# print(total_safe)
print("{:.2f}".format((total_safe*100)/totalGrass(matrix, r)))

# 69.23