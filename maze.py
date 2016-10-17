#! /bin/python

from PIL import Image
import random
c=0
i=0
xy=256
if xy % 2 is not 0:
    xy=xy+1
Matrix = [[[0 for i in range(xy*2)] for i in range(xy*2)] for i in range(xy*2)]

z=int(xy/2)
#print(str(x)+"\t"+str(y)+"\t"+str(z))
#print(Matrix[x][y][z])
#print(Matrix)

water=(10,10,10)
output=7334

for k in range(0,10):
    roomx=random.randint(1,3)+random.randint(1,3)+random.randint(1,9)+random.randint(0,9)
    roomy=random.randint(1,3)+random.randint(1,3)+random.randint(1,9)+random.randint(0,9)
    i=0
    j=0    
    x=random.randint(0,xy)
    y=random.randint(0,xy)
    interrupt=False
    d=0
    
    print("placing room "+str(k)+"["+str(roomx)+","+str(roomy)+"]@"+str(x)+","+str(y))
    
    #Matrix[x][y][z] #room coordinates, top left
    #Matrix[x-1][y+i][z] is 0 if there's no problem on the left. #if it's 1 and there's room on the right move 1
    #Matrix[x-2][y+i][z] is 0 if there's room to move on the left
    #Matrix[x+roomx+1][y+i][z] is 0 if there's no problem on the right #if it's 1 and there's room on the left, move 1
    #Matrix[x+roomx+2][y+i][z] is 0 if there's room to move on the right
    
    step=2
    while (Matrix[x-1][y+i][z] is 1 or Matrix[x+roomx+1][y+i][z] is 1 or Matrix[x+j][y-1][z] is 1 or Matrix[x+j][y+roomy+1][z] is 1) and interrupt is False:
        for i in range(0,roomy):
            for j in range(0,roomx):
                if x<1 or x>xy:
                    print("Room "+str(k)+" left the map")
                    interrupt=True
                    i=roomy
                if y<1 or y>xy:
                    print("Room "+str(k)+" left the map")
                    interrupt=True
                    i=roomy
                if Matrix[x-1][y+i][z] is 1:
                    if Matrix[x+roomx+1][y+i][z] is 1:
                        print("ouch!",d,"room "+str(k))
                        c=x
                        x=y
                        y=c
                        c=0
                        if d >=2 and d<3:
                            interrupt=True
                            print("this doesn't fit | room "+str(k))
                            i=roomy
                        d=d+1
                    elif Matrix[x+roomx+2][y+i][z] is 0:
                        x=x+step
                elif Matrix[x-1][y+i][z] is 0:
                    if Matrix[x+roomx+1][y+i][z] is 1:
                        x=x-step
                if Matrix[x+j][y-1][z] is 1:
                    if Matrix[x+j][y+roomy+1][z] is 1:
                        print("ouch!",d,"room "+str(k))
                        c=x
                        x=y
                        y=c
                        c=0
                        if d >=2 and d<3:
                            interrupt=True
                            print("this doesn't fit | room "+str(k))
                            i=roomy
                        d=d+1
                    elif Matrix[x+j][y+roomy+2][z] is 0:
                        y=y+step
                elif Matrix[x+j][y-1][z] is 0:
                    if Matrix[x+j][y+roomy+1][z] is 1:
                        y=y-step
                
    for i in range(0,roomx):
        for j in range(0,roomy):
            if interrupt is False:
                Matrix[x+i][y+j][z]=k
            else:
                print("we've lost Room "+str(k))
                i=roomx
                #k=k-1
            #Matrix[x-i][y-j][z]=1
    interrupt=False

Btrix=[[0 for i in range(xy)] for i in range(xy)]

countt=0
a=0
b=0
for a in range(0,xy):
    for b in range(0,xy):
        #if Matrix[a][b][z] is not 0:
        for l in range(-1,1):
            for m in range(-1,1):
                if Matrix[a+l][b+m][z] is 0:
                    countt=countt+1
        if countt >=random.randint(1,2) and countt <=random.randint(2,3):
            Btrix[a][b]=1
        countt =0

## imageout
im=None
im=Image.new("RGB",(xy,xy),water)
for a in range(0,xy):
    for b in range(0,xy):
        if Matrix[a][b][z] is not 0:
            im.putpixel((a,b),(50+a,b,50+random.randint(0,z)))
print("./"+str(output)+".png","PNG")
im.save("./"+str(output)+".png","PNG")
im=Image.new("RGB",(xy,xy),water)
for a in range(0,xy):
    for b in range(0,xy):
        if Btrix[a][b] is not 0:
            im.putpixel((a,b),(50+a,b,50+random.randint(0,z)))
print("./"+str(7335)+".png","PNG")
im.save("./"+str(7335)+".png","PNG")
#smatrix(Matrix,output)


#Matrix[a][b][z] #rooms in total values
Ctrix=[[None for i in range(xy)] for i in range(xy)]

coun=0

def crawl(A,B,a,b,z,xy,coun):
    B[a][b]=coun
    for c in range(-1,1):
        for d in range(-1,1):
            if A[a+c][b+d][z] is not 0 and B[a+c][b+d] is None:
                print("tick")
                B=crawl(A,B,a+c,b+d,z,xy,coun)
                #B[a+c][b+d]=coun
    return B



for a in range(0,xy):
    for b in range(0,xy):
        if Matrix[a][b][z] is not 0 and Ctrix[a][b] is None:
            coun=coun+1
        
            #print("crawl the whole room and put it's tiles into Ctrix") ##11
            Ctrix=crawl(Matrix,Ctrix,a,b,z,xy,coun)
            
        else:
            print("done, switching to room: "+str(coun))
    

print(str(Ctrix).replace("None"," ").replace("]","\n"))

im=Image.new("RGB",(xy,xy),water)
print("\nRooms: "+str(coun))
for a in range(0,xy):
    for b in range(0,xy):
        if Ctrix[a][b] is not None:
            im.putpixel((a,b),(Ctrix[a][b],Ctrix[a][b],Ctrix[a][b]))
print("./"+str(7336)+".png","PNG")
im.save("./"+str(7336)+".png","PNG")
