import copy

WYP = [[]]

w = 0

grid = [[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]]

WYP = [[[1, 1, 2.45, 2.4, 2.5, 2.5],    
[1, 2.2, 2.4, 1, 1, 2.5],       
[2.25, 2.2, 2.4, 1, 1.1, 2.55],
[1, 1, 1, 1, 2.1, 2.15],
[1, 1, 1, 1, 2.65, 2.1],
[2.3, 2.35, 2.3, 2.6, 2.6, 2.6]],

[[1, 1, 2.45, 2.4, 2.5, 2.5], 
[1, 2.1, 2.4, 1, 1, 2.5],       
[2.1, 2.15, 2.4, 1, 1.1, 2.55], 
[1, 1, 1, 1, 2.2, 2.2],
[1, 1, 1, 1, 2.65, 2.25],       
[2.3, 2.35, 2.3, 2.6, 2.6, 2.6]]]

e = [0,1,0,-1]
f = [1,0,-1,0]


WOL = []
SPR = []


for pp in range(0,6):
    for qq in range(0,6):
        if grid[pp][qq] == 1.1:
            yp = pp
            xp = qq

start = [yp,xp]

WOL.append(start)

def PATH(WYP3,WOL3,SPR3,w3):
    for cor in WOL3:
        y3 = cor[0]
        x3 = cor[1]
        for s in range (0,4):
            if [y3,x3] not in SPR3:
                SPR3.append([y3,x3])
            if y3+e[s] == -1 or x3+f[s] == -1 or y3+e[s] == 6 or x3+f[s] == 6:
                return False
            war = WYP3[w3][y3+e[s]][x3+f[s]] != 1 and abs(round(round(WYP3[w3][y3+e[s]][x3+f[s]],1)-WYP3[w3][y3+e[s]][x3+f[s]],2)) != 0.05
            if war and [y3+e[s],x3+f[s]] not in WOL3:
                WOL3.append([y3+e[s],x3+f[s]])
    return True


for w in range(0,len(WYP)):
    print(PATH(WYP,WOL,SPR,w))
    if PATH(WYP,WOL,SPR,w):
        for q in WYP[w]:
            fff = 0
print(WOL)
print(SPR)
    