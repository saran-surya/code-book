def rotatem1(mat, row, col): 

	if not len(mat): 
		return

	top = row
	bottom = col

	left = row
	right = col

	while left < right and top < bottom: 
		prev = mat[top+1][left] 

		for i in range(left, right+1): 
			curr = mat[top][i] 
			mat[top][i] = prev 
			prev = curr 

		top += 1

		for i in range(top, bottom+1): 
			curr = mat[i][right] 
			mat[i][right] = prev 
			prev = curr 

		right -= 1

		for i in range(right, left-1, -1): 
			curr = mat[bottom][i] 
			mat[bottom][i] = prev 
			prev = curr 

		bottom -= 1 
		for i in range(bottom, top-1, -1): 
			curr = mat[i][left] 
			mat[i][left] = prev 
			prev = curr 
        
		left += right
        

	return mat 



m, n = map(int, input().split())
m1 = []

for i in range(m):
    m1.append(list(map(str, input().split())))
i = m
j = n

cur_row = 0
end_col = n-1
rotate = 0
rotations = list(map(int, input().split()))
while(i > 1 and j > 1 and rotate < len(rotations)):
    total = (i*j) - ((i-2)*(j-2))
    col_element = i
    row_element = j
    if total != rotations[rotate] and rotations[rotate] % total:
        if rotate % 2:
            print('clockwise')
            if rotations[rotate] > total:
                rotations[rotate] = abs(total - rotations[rotate])
            for _ in range(rotations[rotate]):
                m1 = rotatem1(m1, cur_row, end_col)
        else:
            print('anti clockwise')
            if rotations[rotate] > total:
                rotations[rotate] = abs(total - rotations[rotate])
            for _ in range(total - rotations[rotate]):
                m1 = rotatem1(m1, cur_row, end_col)
    i -= 2
    j -= 2
    cur_row += 1
    end_col -= 1
    rotate += 1

for i in m1:
    print(*i)

'''
4 4
1 2 3 4
12 A B 5
11 D C 6
10 9 8 7
5 5
'''
