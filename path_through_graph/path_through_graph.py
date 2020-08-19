import math
def maxFactor(number):
    maximum = 0
    for i in range(2, 1+(math.ceil(number**0.5))):
        if number % i == 0:
            if number//i > maximum: 
                maximum = number//i
                break
    return maximum if maximum > 0 else 1

graphEdge = 0
n1, n2 = map(int, input().split())
refnode = []
if n1 == n2:
    print(graphEdge)
else:
    flag = True
    while(flag):
        if n1 > n2 and flag:
            while(n1 > n2):
                if maxFactor(n1) == n2:
                    graphEdge += 1
                    flag = False
                    break
                setA = maxFactor(n1)
                graphEdge += 1
                n1 = setA
        elif flag:
            while(n2 > n1):
                if maxFactor(n2) == n1:
                    graphEdge += 1
                    flag = False
                    break
                setA = maxFactor(n2)
                graphEdge += 1
                n2 = setA
    print(graphEdge)