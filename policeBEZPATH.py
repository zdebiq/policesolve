import copy


grid = [[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]

grid = [[1,1,1,0,0,0],
        [0,0,1.1,0,0,0],
        [0,1,1,1,1,0],
        [0,1,0,0,1,0],
        [0,1,0,1,1,0],
        [0,0,0,1,1,0]]

obs = [[[2.1,0],
        [2.15,2.1]],

        [[2.25,0],
        [2.2,2.2]],

        [[2.3,2.35,2.3]],

        [[2.4,0,0],
        [2.45,2.4,2.4]],

        [[0,0,2.5],
        [2.55,2.5,2.5]],

        [[0,2.65,0],
        [2.6,2.6,2.6]]]


a = [1,0,-1,0]
b = [0,1,0,-1]
c = [0,-1,0,1]
d = [1,0,-1,0]

GRID = copy.deepcopy(grid)
pod = copy.deepcopy(grid)
prob = copy.deepcopy(pod)
LOP = [[grid],[],[],[],[],[],[]]
WYP = []


def hit(y0,x0,z0,h0):
    for hy0 in range (0,h0[0]):
        for hx0 in range (0,h0[1]):
            if (y0+a[z0]*hy0+b[z0]*hx0 < 0 or y0+a[z0]*hy0+b[z0]*hx0 > 5 or x0+c[z0]*hy0+d[z0]*hx0 < 0 or x0+c[z0]*hy0+d[z0]*hx0 > 5):
                return False
    return True

def spraw(y1,x1,z1,h1,prob1):
    for hy1 in range(0,h1[0]):
        for hx1 in range (0,h1[1]):
            if (prob1[y1+a[z1]*hy1+b[z1]*hx1][x1+c[z1]*hy1+d[z1]*hx1] > 3):
                return False
    return True

def swyp(p2):
    for q2 in p2:
        for r2 in q2:
            if r2 == 0:
                return False
    return True


print()

for n in range (0,len(obs)):
    for grid in LOP[n]:
        pod = []
        pod = copy.deepcopy(grid)
        h = [len(obs[n]),len(obs[n][0])]
        for y in range (0,6):
            for x in range (0,6):
                for z in range (0,4):
                    if hit(y,x,z,h):
                        prob = []
                        prob = copy.deepcopy(pod)
                        for shy in range (0,h[0]):
                            for shx in range (0,h[1]):
                                prob[y+a[z]*shy+b[z]*shx][x+c[z]*shy+d[z]*shx] += obs[n][shy][shx]
                        if spraw(y,x,z,h,prob):
                            for sshy in range (0,h[0]):
                                for sshx in range (0,h[1]):
                                    pod[y+a[z]*sshy+b[z]*sshx][x+c[z]*sshy+d[z]*sshx] += obs[n][sshy][sshx]
                            LOP[n+1].append(pod)
                            pod = []
                            pod = copy.deepcopy(grid)
    print((len(LOP[n])))


for p in LOP[6]:
    if swyp(p) and p not in WYP:
        WYP.append(p)

