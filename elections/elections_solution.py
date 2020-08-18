n = int(input())
calc = list(input())
v1 = calc.count('A')
v2 = calc.count('B')
i = 0
while(calc[i] == '-'):
    i += 1 
if calc[i] == 'A':
    v1 += i 
start = i 
for j in range(i, n):
    while(i < n):
        if(calc[i] == '-'):
            i += 1
        else:
            break
    if i == n:
        break 
    if calc[i] == 'A':
        if start == i:
            i += 1 
            continue    
        v1 = v1 + (i-start-1)
        start = i 
        i += 1
        continue
    start = i 
    i += 1 
    while(i < n):
        if(calc[i] == '-'):
            i += 1 
        else:
            break
    if i == n:
        v2 = v2+(i-start-1)
    else:
        if calc[i] == 'A':
            v1 = v1+(i-start-1)//2
            v2 = v2+(i-start-1)//2 
            start = i
            i += 1 
        else:
            v2 = v2 + (i-start-1)
if v1 > v2:
    print('A')
elif v2 > v1:
    print('B')
else:
    print('Coalition government')