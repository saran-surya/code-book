def checkscores(points, flag, globalServer):
    if playerA - playerB >= 2 and playerA > 3:
        playerASet.append(1)
        playerBSet.append(0)
        lastScore = ''
        return(0, 0, not globalServer)
    elif playerB - playerA >= 2 and playerB > 3:
        playerBSet.append(1)
        playerASet.append(0)
        lastScore = ''
        return (0, 0, not globalServer)
    return (playerA, playerB, globalServer)

scores = {0:0, 1: 15, 2:30, 3:40}

string = list(map(str, input().split()))
# print(string)
# string = ['Q1', 'Q1', 'Q2', 'Q3', 'O1', 'H2', 'H2', 'Q1', 'Q1', 'Q1', 'Q2']
# string = ['Q1', 'Q1', 'Q3', 'Q3', 'Q1', 'Q1', 'Q3', 'Q3', 'Q1', 'Q1', 'Q3', 'Q3']

i = 0
globalServer = True
initialServe1 = ['Q1', 'Q2']
initialServe2 = ['Q3', 'Q4']
court1 = ['Q1', 'Q2', 'H1']
court2 = ['Q3', 'Q4', 'H2']
outs = ['O1', 'O2']

playerASet = []
playerBSet = []

playerA = 0
playerB = 0

lastScore = ''
server = True
while(i < len(string)):
    print(string[i])              #Comment this line out
    if server and globalServer:
        if string[i] not in initialServe2:
            if lastScore == '':
                lastScore = string[i]
            else:
                lastScore = ''
                playerB += 1
                playerA, playerB, globalServer = checkscores(playerB, False, globalServer)
        elif string[i] in initialServe2:
            lastScore = string[i]
            server = False
        elif string[i] in court2:
            lastScore = string[i]
            server = False
        elif string[i] in outs:
            lastScore = ''
            playerB += 1
            playerA, playerB, globalServer = checkscores(playerB, False, globalServer)
    elif not server and globalServer:
        if string[i] in court1:
            lastScore = string[i]
        elif string[i] in court2:
            lastScore = ''
            playerA += 1
            playerA, playerB, globalServer = checkscores(playerA, True, globalServer)
        elif string[i] in outs:
            lastScore = ''
            playerA += 1
            playerA, playerB, globalServer = checkscores(playerA, True, globalServer)
        server = True
    elif server and not globalServer:
        print('Set two')
        if string[i] not in initialServe1:
            if lastScore == '':
                lastScore = string[i]
            else:
                lastScore = ''
                playerA += 1
                playerA, playerB, globalServer = checkscores(playerA, True, globalServer)
        elif string[i] in initialServe1:
            lastScore = string[i]
            server = False
        elif string[i] in court1:
            lastScore = string[i]
            server = False
        elif string[i] in outs:
            lastScore = ''
            playerA += 1
            playerA, playerB, globalServer = checkscores(playerA, True, globalServer)
    elif not server and not globalServer:
        print('set two')
        if string[i] in court2:
            lastScore = string[i]
        elif string[i] in court1:
            lastScore = ''
            playerB += 1
            playerA, playerB, globalServer = checkscores(playerB, False, globalServer)
        elif string[i] in outs:
            lastScore = ''
            playerB += 1
            playerA, playerB, globalServer = checkscores(playerB, False, globalServer)
        server = True
    i += 1

print('--------------------op----------------')
if globalServer:
    print(*playerASet if playerASet != [] else '0')
    print(*playerBSet if playerBSet != [] else '0')
    if playerA == playerB and playerA > 2:
        print('Deuce')
    elif playerA > playerB and playerA > 3:
        print('Advantage Server' if globalServer else 'Advantage Reciever')
    elif playerA < playerB and playerB > 3:
        print('Advantage Reciever' if globalServer else 'Advantage Server')
    else:
        print(scores[playerA], scores[playerB])
else:
    print(*playerBSet if playerBSet != [] else '0')
    print(*playerASet if playerASet != [] else '0')
    if playerA == playerB and playerB > 2:
        print('Deuce')
    elif playerA > playerB and playerB > 3:
        print('Advantage Reciever' if globalServer else 'Advantage Server')
    elif playerA < playerB and playerB > 3:
        print('Advantage Server' if globalServer else 'Advantage Reciever')
    else:
        print(scores[playerB], scores[playerA])