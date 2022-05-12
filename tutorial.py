import time
#from tkinter import *
#from tkinter import messagebox
import tkinter as tk

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

#rozw = [[1,1,1,2.15,2.1,2.6],[2.2,2.25,1.1,2.1,2.65,2.6],[2.2,1,1,1,1,2.6],[2.55,1,2.45,2.4,1,2.3],[2.5,1,2.4,1,1,2.35],[2.5,2.5,2.4,1,1,2.3]] 
rozw = [[[1,1,1,0,0,0],[0,0,1.1,0,0,0],[0,1,1,1,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,0,0,1,1,0]],
[[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]],
[[1,1,1,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1.1,0,1],[0,0,0,1,1,1]]]

win = tk.Tk()
 
win.geometry("600x600")
  
win.title("Permutations:")



canvas = tk.Canvas(win,width = 600,height = 600)
canvas.pack()

print(rozw[0][0][4])

for n in range(0,3):
    for ky in range(0,6):
        for kx in range(0,6):
            #print(ky,kx)
            canvas.create_rectangle(100*kx,100*ky,100*(kx+1),100*(ky+1), fill= kolor[str(rozw[n][ky][kx])])
    time.sleep(1)
    win.update()
win.mainloop()