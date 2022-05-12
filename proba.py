
for hy4 in range(0,h1[0]):
        for hx4 in range (0,h1[1]):
            if (prob1[y4+a[z1]*hy4+b[z1]*hx4][x4+c[z1]*hy4+d[z1]*hx4] > 3):
                return False
    return True







