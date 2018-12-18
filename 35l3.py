#! /bin/python

from random import randint
from PIL import Image

class Room:
	def __init__(self, iD=0, position=[0,0], size=[0,0], exits=[], neighbors=[]):
		self.iD = iD
		self.position = position
		self.size = size
		self.exits = exits
		self.neighbors = neighbors
	def __int__(self):
		return self.iD
	def __str__(self):
		return str(iD + "\nsize:" + size + "\n")

def walk(Map, room, location, action):
	countNone = 0
	for x in range(location[0], location[0]+room.size[0]):
		for y in range(location[1], location[1]+room.size[1]):
			if Map[x][y]:
				countNone += 1
			if action:
				if x == location[0] or x == location[0]+room.size[0]-1:
					Map[x][y] = 999
				elif y == location[1] or y == location[1]+room.size[1]-1:
					Map[x][y] = 999
				else:
					Map[x][y] = action
	if action:
		return Map
	else:
		return countNone

def placeRooms(Map, roomList, xy):
	if not Map:
		Map = [[None for x in range(xy[0])] for x in range(xy[1])]
	for room in roomList:
		placed = False
		xy = [0,0]
		while not placed:
			if walk(Map, room, xy, None) == 0:
				Map = walk(Map, room, xy, room.iD)
				placed = True
			elif xy[0] + room.size[0] > len(Map)-1:
				xy[0] = 0
				xy[1] += 1
			elif xy[1] + room.size[1] > len(Map[0])-1:
				placed = True
			else:
				xy[0] += 1
	return Map

def generateRooms(numberOfRooms, minsize, maxsize):
	roomList = []
	for room in range(1, numberOfRooms):
		roomList.append(Room(iD=room, 
			size=[randint(minsize[0], maxsize[0]), 
					randint(minsize[1], maxsize[1])]
				))
	return roomList

def bimage(Map, name):
	im=None
	im=Image.new("RGB",(len(Map), len(Map[0])),(0xFF, 0xFF, 0xFF))
	for x in range(0, len(Map)):
		for y in range(0, len(Map[0])):
			if Map[x][y]:
				if Map[x][y] == 999:
					im.putpixel((x,y), (0xFF, 0x00, 0x00))
				else:
					im.putpixel((x,y), (0x00, 0x00, 0x00))
	im.save("./"+str(name)+".png","PNG")


def main():
	xy = [64, 64]
	Map = [[None for x in range(xy[0])] for x in range(xy[1])]
	rooms = generateRooms(128, [5,5], [32,32])
	Map = placeRooms(Map, rooms, xy)
	
	bimage(Map, "maze")
	pass

main()