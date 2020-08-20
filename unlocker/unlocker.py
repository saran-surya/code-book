import copy

def clockwise(row, col, skips):
    print(row, col, 'row-col')
    for x in range(row, col+1):
        print(m1[x])
        for y in range(row, col+1):
            if x == row:
                print('first row', m1[x][y])
            elif y == col and x != row:
                print('last column', m1[x][y])
            elif y == row and x != col:
                print('first column', m1[x][y])
            elif x == col:
                print('last row', m1[x][y])

m, n = map(int, input().split())
m1 = []
for i in range(m):
    tem = (list(map(str, input().split())))
    m1.append(tem)
ref = copy.deepcopy(m1)
rotations = list(map(int, input().split()))
for i in m1:
    print(i)

i = m
j = n

cur_row = 0
end_col = n-1
rotate = 0

while(i > 1 and j > 1):
    total = (i*j) - ((i-2)*(j-2))
    if total != rotations[rotate]:
        if rotate % 2:
            print('clockwise')
        else:
            clockwise(cur_row, end_col, rotations[rotate])
            print('anti-clockwise')
    i -= 2
    j -= 2
    cur_row += 1
    end_col -= 1
    rotate += 1
print('-----------------------')
for i in m1:
    print(i)

'''
4 4
1 2 3 4
12 A B 5
11 D C 6
10 9 8 7
2 2
'''
