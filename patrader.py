#! /bin/python

import math
import random
from PIL import Image

class town:
    def __init__(self):
        self.name="townname"
        self.coords=0,0
        self.population=[]


def smooth(M,x,y):
    #print(M[x][y])
    if M[x][y] >= 2:
        for j in range (0,M[x][y]+random.randint(1,5)):
            for k in range (0,M[x][y]+random.randint(1,5)):
                r=random.randint(7,10)
                if M[x][y]-(j+k) >= 2:
                    if M[x][y]-(j+k)+M[x+j][y+k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x+j][y+k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x+j][y+k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x-j][y-k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x-j][y-k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x-j][y-k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x+j][y-k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x+j][y-k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x+j][y-k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x-j][y+k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x-j][y+k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x-j][y+k]=M[x][y]-(j+k)+random.randint(1,2)

def bterrain(xy, Matrix, x, y, mutator):
    za=0
    zb=0
    for i in range (0,mutator):
        if i%(xy*int(xy/random.randint(5,30))) is 0:
            print("ding!")
            za=random.randint(0,3)
            zb=random.randint(0,3)
        x=random.randint(5,(xy/2)-5)+random.randint(5,(xy/2)-5)+(xy*za)
        y=random.randint(5,(xy/2)-5)+random.randint(5,(xy/2)-5)+(xy*zb)
        Matrix[x][y]=random.randint(-5,5)
        smooth(Matrix,x,y)
        #'''
    for m in range (0,int(mutator/random.uniform(1.0,2.0))):
        x=random.randint(5,(xy*2)-5)+random.randint(5,(xy*2)-5)
        y=random.randint(5,(xy*2)-5)+random.randint(5,(xy*2)-5)
        Matrix[x][y]=random.randint(0,5)
        smooth(Matrix,x,y)
    return Matrix

def bimage(xy,Matrix,water,output):
    im=None
    im=Image.new("RGB",(xy*4,xy*4),water)
    for a in range(0,xy*4):
        for b in range(0,xy*4):
            if Matrix[a][b] >= 1:
                im.putpixel((a,b),(Matrix[a][b]*10+100,Matrix[a][b]*10+50,0))
            '''
            if Matrix[a][b] <= 0:#
                q=None
            elif Matrix[a][b] <= 3:
                im.putpixel((a,b),(210-Matrix[a][b],(Matrix[a][b]*10)+155,60))
            elif Matrix[a][b] <= 6:
                im.putpixel((a,b),(90,(Matrix[a][b]*10)+155,20))
            elif Matrix[a][b]<=9:
                im.putpixel((a,b),((Matrix[a][b]*10)+130,(Matrix[a][b]*10)+155,(Matrix[a][b]*10)+140))
            elif Matrix[a][b] >= 10:
                im.putpixel((a,b),(140,155+Matrix[a][b],150))
                #'''
    im.save("/usr/home/g/pat/"+str(output)+".png","PNG")

def init():
    xy=32
    mutator=int(xy*xy*random.uniform(1.0,2.0))
    land=(200,150,0)
    water=(0,50,0)
    Matrix = [[0 for x in range(xy*4)] for x in range(xy*4)]
    x=0
    y=0
    maps=50
    start=750
    for u in range (start,start+maps):
        bimage(xy,bterrain(xy,[[0 for x in range(xy*4)] for x in range(xy*4)],x,y,mutator),water,u)

init()
