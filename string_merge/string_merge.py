def check(line):
    i = 0
    j = 0
    backup = line.copy()
    stack = []
    while(j < len(line) and i < len(string)):
        if string[i] in line and stack == []:
            stack.append(string[i])
            line[line.index(string[i])] = '-'
            j += 1 
        elif string[i] in line and stack[-1] == string[i-1]:
            stack.append(string[i])
            line[line.index(string[i])] = '-'
            j += 1
        else:
            stack = []
            line = backup.copy()
            j = 0
        i += 1
    if len(stack) == len(line) and stack != []:
        return True
    return False
string = input()
totalLen = len(string)
for i in range(int(input())):
    temp = list(input())
    if check(temp):
        totalLen -= len(temp)
if totalLen == 0:
    print('YES')
else:
    print('NO')


