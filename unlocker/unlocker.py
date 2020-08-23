import copy

# This code needs editing ~ Saran


# def check_f_top(index_x, index_y, row, col, skips, flag = 'row'):
#     print('------------------ in top --------------------')
#     if flag == 'row':
#         print('----> row main <----')
#         temp = col - (((index_x + skips) - col) - col)
#         if temp >= row:
#             m1[temp][row] = ref[index_x][index_y]
#             return True
#         else:
#             print('Cannot add')
#     elif flag == 'col':
#         print(ref[index_x][index_y])
#         print(index_x + skips)
#         print(index_y + skips)
#         temp = col - (index_y + skips)
#         if temp >= row:
#             m1[temp][row] = ref[index_x][index_y]
#     else:
#         print(index_y + skips)
#         print((index_y + skips) - col)
#         temp = ((index_y + skips) - col) - col
#         if col - (temp - col) >= row:
#             m1[col-(temp - col)][row] = ref[index_x][index_y]
#             return True
#         else:
#             return check_f_right(index_x, index_y, row, col, skips, False)


# def check_f_left(index_x, index_y, row, col, skips, flag = 'row'):
#     print('-------------- in left -------------')
#     if flag == 'row':
#         pass
#     else:
#         temp = (index_y + skips) - col
#         if col - abs(temp - col) >= row:
#             m1[col][col-abs(temp-col)] = ref[index_x][index_y]
#             return True
#         else:
#             return check_f_top(index_x, index_y, row, col, skips, False)

# def check_f_down(index_x, index_y, row, col, skips, flag = 'row'):
#     print('---------------- in down -------------')
#     if flag == 'row':
#         print('-----> main')
#         print(ref[index_x][index_y])
#         print(index_x)
#         print(index_x + skips)
#         print((index_x + skips) - col)
#         temp = col - ((index_x + skips) - col)
#         if temp >= row and temp <= col:
#             m1[col][temp] = ref[index_x][index_y]
#             return True
#         else:
#             return check_f_left(index_x, index_y, row, col, skips, 'row')

#     else:
#         if (index_y + skips) - col <= col:
#             m1[(index_y + skips) - col][col] = ref[index_x][index_y]
#             return True
#         else:
#             return check_f_left(index_x, index_y, row, col, skips, False)

# def check_f_right(index_x, index_y, row, col, skips, flag = 'row'):
#     if flag == 'row':
#         print('---------------- in right -----------------')
#         print(index_x, index_y)
#         print((index_y + skips))
#         if index_y + skips <= col:
#             m1[index_x][index_y + skips] = ref[index_x][index_y]
#             return True
#         return check_f_down(index_x, index_y, row, col, skips, False)
#     else:
#         print('************ right else ************')
#         if abs(total - (index_y + skips)) <= col:
#             m1[row][abs(total - (index_y + skips))] = ref[index_x][index_y]
#    
#          return True
changed = []

def tem_reducer(temp, col):
    while(temp > col*2):
        temp -= col*2
    return temp

def tem_1_reducer(temp, col):
    while(temp > col):
        temp -= col
    return temp


def right(index_x, index_y, row, col, skips, max_row, max_col):
    print('element ====================== right ', ref[index_x][index_y])
    print('mrc', max_row, max_col)
    tem = index_y + skips
    print('Tem -------> ', tem)
    if tem <= col:
        m1[row][tem] = ref[index_x][index_y]
        changed.append(ref[index_x][index_y])
    else:
        return down(index_x, index_y, row, col, abs(tem-col), max_row, max_col)
def down(index_x, index_y, row, col, skips, max_row, max_col):
    print('element ====================== down ', ref[index_x][index_y])
    tem = index_x + skips
    print('Tem -------> ', tem)
    if tem <= col:
        m1[tem][col] = ref[index_x][index_y]
        changed.append(ref[index_x][index_y])
    else:
        pass
        return left(index_x, index_y, row, col, abs(tem-col), max_row, max_col)
        
def left(index_x, index_y, row, col, skips, max_row, max_col):
    print('element ====================== left ', ref[index_x][index_y])
    print(skips, 'skips')
    tem = index_y - skips
    print('Tem', tem)
    print('mrc', max_row, max_col)
    if tem >= row:
        m1[col][tem] = ref[index_x][index_y]
        changed.append(ref[index_x][index_y])
    else:
        pass
        # return top(index_x, index_y, row, col, skips, max_row + col_element - 1, max_col + row_element - 1)
def top(index_x, index_y, row, col, skips, max_row, max_col):
    print('element ====================== top ', ref[index_x][index_y])
    tem = index_x - skips
    print('Tem', tem)
    print('mrc', max_row, max_col)
    if tem >= row:
        m1[tem][row] = ref[index_x][index_y]
        changed.append(ref[index_x][index_y])
    else:
        pass
        # return right(index_x, index_y, row, col, skips, max_row + col_element - 1, max_col + row_element - 1)

def clockwise(row, col, skips, col_element, row_element):
    # inverted row to column for better results
    print(row_element, 'row element ------<')
    print(col_element, 'col element <-----')
    print(row, col, 'row-col')
    for x in range(row, col+1):
        for y in range(row, col+1):
            if x == row:
                print('first row', ref[x][y])
                right(x, y, row, col, skips, row_element, col_element)
            elif y == col and x != row and x != col:
                print('last column', ref[x][y])
                down(x, y, row, col, skips, row_element , col_element )
            elif y == row and x != col and x != row:
                print('first column', ref[x][y])
                # top(x, y, row, col, skips, row_element, col_element)
            elif x == col:
                print('last row', ref[x][y])
                left(x, y, row, col, skips, row_element, col_element)

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

while(i > 1 and j > 1 and rotate < len(rotations)):
    total = (i*j) - ((i-2)*(j-2))
    col_element = i
    row_element = j
    if total != rotations[rotate] and rotations[rotate] % total:
        if rotate % 2:
            print('clockwise')
            # if rotations[rotate] > total:
            #     rotations[rotate] = abs(total - rotations[rotate])
            # clockwise(cur_row, end_col, rotations[rotate], i, j)
        else:
            if rotations[rotate] > total:
                rotations[rotate] = abs(total - rotations[rotate])
            print(rotations[rotate])
            clockwise(cur_row, end_col, rotations[rotate], i, j)
            print('anti-clockwise')
    i -= 2
    j -= 2
    cur_row += 1
    end_col -= 1
    rotate += 1
print('---------- OP -------------')
for i in m1:
    print(i)
print()
print(changed)

'''
4 4
1 2 3 4
12 A B 5
11 D C 6
10 9 8 7
5 5
'''
