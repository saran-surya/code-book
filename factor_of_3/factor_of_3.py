def checkIfpossible():
    maximum = -1
    ind = -1
    for j in range(n):
        if (stack[-1]+array[j]) %3 != 0 and j not in indexes:
            if maximum < array[j]:
                maximum = array[j]
                ind = j
    return False if ind == -1 else ind

def permute():
    i = 0
    while(i < n):
        if stack == []:
            stack.append(array[i])
            indexes.append(i)
        elif stack != []:
            ele = checkIfpossible()
            if ele:
                stack.append(array[ele])
                indexes.append(ele)
        i += 1


# n = 4
# array = [3, 6, 1, 9]
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    indexes = []
    stack = []
    permute()
    if len(stack) < n:
        print('NO')
    else:
        print('YES')

################################ For Further Updates ############################################3

# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)

# totalPermutations = factorial(n)
# print(totalPermutations)