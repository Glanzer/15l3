#! /bin/python

import random
from PIL import Image

def pmatrix(M):
    print(" "+str(M).replace("],","\n").replace("[","").replace(","," ").replace("]","").replace("'",""))

def walk(B,M,px,py):
    fin=False
    B[px][py]=M[px][py]
    for x in range(-1,2):
        for y in range(-1,2):
            if (px+x<len(M[0])-1 and py+y<len(M[0])-1) and (px+x>0 and py+y>0):
                if (M[px+x][py+y] is not 0) and (B[px+x][py+y] is 0):
                    B=walk(B,M,px+x,py+y)
    return B

def bimage(M,name,xy,j):
    im=None
    im=Image.new("RGB",(len(M[0]),len(M[0])),(100,0,100))
    for x in range(0,len(M[0])):
        for y in range(0,len(M[0])):
            #print(x,y,M[x][y])
            if M[x][y] is j:
                im.putpixel((x,y),(250,100,0))
            else:
                im.putpixel((x,y),(M[x][y]*3,M[x][y]*4,M[x][y]*2))
    #im.show()
    im.save("./"+str(name)+".png","PNG")

class room():
    level=[]
    def __init__(self,name):
        self.name=None
        self.cords=[]
        self.exits=[]
        self.nghbr=[]

def sorms(rms,tarjay):
    j=None
    for i in range(0,len(rms)):
        if rms[i].name is tarjay:
            j=i
    return j

def place_rooms(rooms,xy):
    Matrix = [[0 for x in range(xy[0])] for x in range(xy[1])]
    for i in range(0,rooms):
        roomx = random.randint(0,xy[0])
        roomy = random.randint(0,xy[1])
        roomsx = random.randint(1,8)+random.randint(1,4)+random.randint(1,4)
        roomsy = random.randint(1,8)+random.randint(1,4)+random.randint(1,4)
        if roomx+roomsx > xy[0]:
            roomx=roomx-(roomx+roomsx-xy[0])
        elif roomx < 1:
            roomx+=1
        if roomy+roomsy > xy[1]:
            roomy=roomy-(roomy+roomsy-xy[1])
        elif roomy < 1:
            roomy+=1
        for x in range(0,roomsx):
            if (Matrix[roomx+x][roomy-1] is not 0) and (roomy+roomsy) <= xy[1]:
                roomy=roomy-1
        for y in range(0,roomsy):
            if (Matrix[roomx-1][roomy+y] is not 0) and (roomx+roomsx) <= xy[0]:
                roomx=roomx-1
        for x in range(0,roomsx):
            for y in range(0,roomsy):
                Matrix[roomx+x][roomy+y]=i
    return Matrix

def fix_walls(M,xy):
    for x in range(0,xy[0]):
        for y in range(0,xy[1]):
            chc=0
            '''
            for j in range(-1,2):
                for k in range(-1,2):
                    if (x+j<xy[0] and y+k<xy[1]) and (x+j>0 and y+k>0):
                        if (M[x+j][y+k] is not 0) and (M[x+j][y+k] is not M[x][y]):
                            chc=chc+1
            #print(str(chc)+"\t"+str(x)+"/"+str(y))
            if chc > 1: M[x][y]=0
            chc=0
            '''
            if M[x][y] is not 0:
                for j in range(-1,2):
                    for k in range(-1,2):
                        if (x+j<xy[0] and y+k<xy[1]) and (x+j>0 and y+k>0):
                            if (M[x+j][y+k] is not M[x][y])and(M[x+j][y+k] is not 0):
                                chc+=1
            if chc > 1: M[x][y]=0
            chc=0
            if M[x][y] is not 0:
                for j in range(-1,2):
                    for k in range(-1,2):
                        if (x+j<xy[0] and y+k<xy[1]) and (x+j>0 and y+k>0):
                            if (M[x+j][y+k] is not M[x][y])and(M[x+j][y+k] is not 0):
                                chc+=1
            if chc > 0: M[x][y]=0
            '''
            if (M[x][y] %2 is 0):
                if chc < 4: M[x][y]=0
            else:
                if chc < 3: M[x][y]=0
            '''
    return M


def get_rooms(Matrix,xy):
    rmlist=[]
    rms=[]
    Btrix = [[0 for x in range(xy[0])] for x in range(xy[1])]
    Matrix=fix_walls(Matrix,xy)
    #pmatrix(Matrix)
    for x in range(1,xy[0]):
        for y in range(1,xy[1]):
            if Matrix[x][y] is not 0 and Btrix[x][y] is 0:
                Btrix=walk(Btrix,Matrix,x,y)
                if Btrix[x][y] not in rmlist:
                    rmlist.append(Btrix[x][y])
                    rms.append(room(Btrix[x][y]))
                    rms[len(rms)-1].name=Btrix[x][y]
                    rms[(len(rms)-1)].cords.append([x,y])
                    
                    #print(rms[sorms(rms,Btrix[x][y])].cords)
                else:
                    rms[sorms(rms,Btrix[x][y])].cords.append([x,y])
    #print(rms[0]) #did we make everything 0?
    rms[0].level=Btrix
    return rms




### Initialization
xy = (64,64)
rooms=32
###placing rooms
Matrix=place_rooms(rooms,xy)
###walking and numbering rooms
Rooms=get_rooms(Matrix,xy)


rmlist=[]
for i in range(0,len(Rooms)):rmlist.append(Rooms[i].name)
#print(rmlist)
rmlist.sort()
print(rmlist)
print("\n")

bimage(Rooms[0].level,"map",xy,Rooms[0].name)

#'''
memo=[]
for x in range(0,xy[0]):
    for y in range(0,xy[1]):
        count=[0,0]
        rooms=[]
        if Rooms[0].level[x][y] is 0:
            for j in range(-1,2):
                for k in range(-1,2):
                    if (x+j>0 and y+k>0)and(x+j<len(Rooms[0].level[0])and y+k<len(Rooms[0].level[0])):
                        if (Rooms[0].level[x+j][y+k] is 0) and ([x+j,y+k] not in memo): 
                            if j is 0: count[0]=count[0]+1
                            if k is 0: count[1]=count[1]+1
                        elif (Rooms[0].level[x+j][y+k] is not 0) and (Rooms[0].level[x+j][y+k] not in rooms):
                            rooms.append(Rooms[0].level[x+j][y+k])
        #if len(rooms)>1:print(str(rooms)+"\t\t"+str(x)+"/"+str(y))
            #print(count)
        #print(count)
        if (count[0]is 3 or count[1]is 3)and len(rooms)>1:
            memo.append([rooms,[x,y]])
#print(memo)
#memo[i][0][0]  -> possible Room connecting
#memo[i][0][1]  -> possible Target-room
#memo[i][1]     -> possible Doorway coordinates
#memo[i]        -> possibility #i

for i in range(0,len(rmlist)):
    for j in range(0,len(memo[0])):
        if Rooms[i].name in memo[j][0]:
            Rooms[i].exits.append(memo[j])


for i in range(0,len(rmlist)):
    print("Room: "+str(Rooms[i].name)+"\t"+str(Rooms[i].exits))

#'''
