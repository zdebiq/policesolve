import copy
from PIL import Image
from PIL import ImageDraw
import time
import tkinter as tk

startcz = time.time()

poziomy = {
    '0': [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
    '1': [[1,1,1,0,0,0],[0,0,1.1,0,0,0],[0,1,1,1,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,0,0,1,1,0]],
    '2': [[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]],
    '3': [[1,1,1,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1.1,0,1],[0,0,0,1,1,1]],
    '14': [[1,1,1,0,0,1],[0,0,0,0,1,1],[1,1,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,1.1,1],[0,0,0,1,1,1]],
    '48': [[1,1,1,1,1,0],[1,0,1.1,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,1,0],[1,1,0,0,1,1]],
    '60': [[1,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,1.1,0,0],[1,1,0,0,0,1],[1,1,1,1,1,1]]
}
grid = poziomy['60']

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

obs.reverse()

kolor = {
    '0':'#707B7C',
    '1':'#212F3D',
    '1.1':'#FFFFFF',
    '2.1':'#E74C3C',
    '2.15':'#78281F',
    '2.2':'#E67E22',
    '2.25':'#784212',
    '2.3':'#F1C40F',
    '2.35':'#B7950B',
    '2.4':'#2ECC71',
    '2.45':'#1D8348',
    '2.5':'#3498DB',
    '2.55':'#21618C',
    '2.6':'#8E44AD',
    '2.65':'#4A235A',
}

a = [1,0,-1,0]
b = [0,1,0,-1]
c = [0,-1,0,1]
d = [1,0,-1,0]

e = [0,1,0,-1]
f = [1,0,-1,0]

path = copy.deepcopy(grid)
pod = copy.deepcopy(grid)
prob = copy.deepcopy(pod)
LOP = [[grid],[],[],[],[],[],[]]
WYP = []
WOL = []
SPR = []


for pp in range(0,6):
    for qq in range(0,6):
        if grid[pp][qq] == 1.1:
            yp = pp
            xp = qq

start = [yp,xp]

WOL.append(start)


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

def PATH(WYP3,WOL3,SPR3,w3):
    for cor in WOL3:
        y3 = cor[0]
        x3 = cor[1]
        for s in range (0,4):
            if y3+e[s] == -1 or x3+f[s] == -1 or y3+e[s] == 6 or x3+f[s] == 6:
                return False
            war = WYP3[w3][y3+e[s]][x3+f[s]] != 1 and abs(round(round(WYP3[w3][y3+e[s]][x3+f[s]],1)-WYP3[w3][y3+e[s]][x3+f[s]],2)) != 0.05
            if war and [y3+e[s],x3+f[s]] not in WOL3:
                WOL3.append([y3+e[s],x3+f[s]])
            if [y3,x3] not in SPR3:
                SPR3.append([y3,x3])
    return True

def pust(y5,x5,z5,h5,prob5):
    for hy5 in range(-1,h5[0]+1):
        for hx5 in range(-1,h5[1]+1):
            try:
                zero = prob5[hy5][hx5] == 0
                somsiady = prob[hy5+1][hx5] != 0 and prob[hy5-1][hx5] != 0 and prob[hy5][hx5+1] != 0 and prob[hy5][hx5-1] != 0
                if zero and somsiady:
                    return False
            except:
                print("except")
    return True

win = tk.Tk()
 
win.geometry("600x600")
  
win.title("Permutations:")

canvas = tk.Canvas(win,width = 600,height = 600)
canvas.pack()

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
                            for ky in range(0,6):
                                for kx in range(0,6):
                                    canvas.create_rectangle(100*kx,100*ky,100*(kx+1),100*(ky+1), fill= kolor[str(pod[ky][kx])])
                            win.update()
                            pod = []
                            pod = copy.deepcopy(grid)

win.destroy()

win.mainloop()

for p in LOP[6]:
    if swyp(p) and p not in WYP:
        WYP.append(p)

for w in range(0,len(WYP)):
    WOL = []
    WOL.append(start)
    if PATH(WYP,WOL,SPR,w):
        rozw = WYP[w]


img = Image.new("RGB",(600,600))

img1 = ImageDraw.Draw(img) 


for rz in range(0,len(rozw)):
    for sz in range(0,len(rozw[rz])):
          img1.rectangle([(100*sz, 100*rz), (100*(sz+1), 100*(rz+1))], fill = kolor[str(rozw[rz][sz])])

img.show()


end = time.time()
print(end-startcz)

