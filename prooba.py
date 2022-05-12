import pyglet
#from pyglet import shapes
import time

kolorgb = {
    '0':(112, 123, 124),
    '1':(33, 47, 60),
    '1.1':(255,255,255),
    '2.1':(231, 76, 60),
    '2.15':(120, 40, 31),
    '2.2':(230, 126, 34),
    '2.25':(120, 66, 18),
    '2.3':(241, 196, 15),
    '2.35':(183, 149, 11),
    '2.4':(46, 204, 113),
    '2.45':(29, 131, 72),
    '2.5':(52, 152, 219),
    '2.55':(33, 97, 140),
    '2.6':(142, 68, 173),
    '2.65':(74, 35, 90),
}

rozw = [[[1,1,1,0,0,0],[0,0,1.1,0,0,0],[0,1,1,1,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,0,0,1,1,0]],
[[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]],
[[1,1,1,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1.1,0,1],[0,0,0,1,1,1]]]

recta = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
'''
def driw(rozw5):
    for rz5 in range(0,len(rozw5)):
        for sz5 in range(0,len(rozw5[rz5])):
            recta[rz5][sz5] = shapes.Rectangle(100*sz5, 500-100*rz5, 100, 100, color= kolorgb[str(rozw5[rz5][sz5])], batch=batch)
'''
window = pyglet.window.Window()#600,600)
#batch = pyglet.graphics.Batch()

v = 0

'''
def update(dt):
    window.clear()
    batch.draw()
    driw(rozw[v])
    if v >= len(rozw):
        exit()
    v += 1

def update(dt):
    window.clear()
    label.draw()
    label = pyglet.text.Label(str(v),
                            font_name='Times New Roman',
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')
    label.draw()
    v += 1

startcz = time.time()

def update(dt):
    label = pyglet.text.Label(str(round(time.time()-startcz,3)),font_name='Times New Roman',font_size=32,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
    window.clear()
    label.draw()
    print(time.time()-startcz)

'''

#startcz = time.time()

@window.event
def on_draw():
    for n in range(0,5):
        window.clear()
        label = pyglet.text.Label(str(n),font_name='Times New Roman',font_size=72,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
        label.draw()
        print(n)
        time.sleep(1)

#pyglet.clock.schedule_interval(update, 1)

pyglet.app.run()


















import pyglet
from pyglet import shapes
import time

kolorgb = {
    '0':(112, 123, 124),
    '1':(33, 47, 60),
    '1.1':(255,255,255),
    '2.1':(231, 76, 60),
    '2.15':(120, 40, 31),
    '2.2':(230, 126, 34),
    '2.25':(120, 66, 18),
    '2.3':(241, 196, 15),
    '2.35':(183, 149, 11),
    '2.4':(46, 204, 113),
    '2.45':(29, 131, 72),
    '2.5':(52, 152, 219),
    '2.55':(33, 97, 140),
    '2.6':(142, 68, 173),
    '2.65':(74, 35, 90),
}

rozw = [[[1,1,1,0,0,0],[0,0,1.1,0,0,0],[0,1,1,1,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,0,0,1,1,0]],
[[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]],
[[1,1,1,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1.1,0,1],[0,0,0,1,1,1]]]

recta = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
'''
def driw(rozw5):
    for rz5 in range(0,len(rozw5)):
        for sz5 in range(0,len(rozw5[rz5])):
            recta[rz5][sz5] = shapes.Rectangle(100*sz5, 500-100*rz5, 100, 100, color= kolorgb[str(rozw5[rz5][sz5])], batch=batch)
'''
window = pyglet.window.Window()#600,600)
#batch = pyglet.graphics.Batch()

v = 0

'''
def update(dt):
    window.clear()
    batch.draw()
    driw(rozw[v])
    if v >= len(rozw):
        exit()
    v += 1

def update(dt):
    window.clear()
    label.draw()
    label = pyglet.text.Label(str(v),
                            font_name='Times New Roman',
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')
    label.draw()
    v += 1

startcz = time.time()

def update(dt):
    window.clear()
    label = pyglet.text.Label(str(round(time.time()-startcz,3)),font_name='Times New Roman',font_size=32,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
    label.draw()
    print(time.time()-startcz)


label1 = pyglet.text.Label(str(round(time.time()-startcz,3)),font_name='Times New Roman',font_size=72,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label1.draw()

pyglet.clock.schedule_interval(update, 1)

pyglet.app.run()

'''
























import turtle

LOP = [[[1,1,1,0,0,0],[0,0,1.1,0,0,0],[0,1,1,1,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,0,0,1,1,0]],
[[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,1.1,0],[1,1,1,1,0,0],[1,1,1,1,0,0],[0,0,0,0,0,0]],
[[1,1,1,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1.1,0,1],[0,0,0,1,1,1]]]

t = turtle.Turtle()

#turtle.bgcolor('black')
#ht()
t.pu()
t.setpos(-300,300)
t.pd()
for ky in range(0,6):
    for kx in range(0,6):
        t.pd()
        for kz in range(0,4):
            t.fd(100)
            t.rt(90)
        
        t.pu()
        t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(600)
    t.rt(180)