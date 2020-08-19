import math
low, high = map(int, input().split())
k = int(input())
cc = 0
for i in range(low, high+1):
    if i%2 == 0:
        cc += 1
total = (high-low + 1) 
res = int(math.pow(total, k-1) * cc) % 10000000007
print(str(res))