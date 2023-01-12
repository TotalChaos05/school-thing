from Graphics import *
from random import randint
from math import pi
debug=True
class cursor:
	def __init__(self,x,y,chance):
		self.x=x
		self.y=y
		self.chance = chance
		self.num = None
		penup()
	def upd(self):
		goto(getX(self.x), getY(self.y))
		if debug==True:
			print(self.x, self.y, "rand", self.num, self.chance)

	def drawRandDune(self):
		self.upd()
		pendown()
		begin_fill()
		pensize(20)
		while self.x <=1300:
			self.num=randint(0,100)
			if self.chance>self.num:
				self.x+=100
				self.y-=75
				self.upd()
				self.x+=100
				self.y+=75
				self.upd()
			else:
				self.x+=50
				self.upd()
		goto(getX(1300),getY(700))
		goto(getX(0),getY(700))
		end_fill()



def dune():
	#far back
	color('#8A3909')
	backdune = cursor(0,350,50)
	backdune.drawRandDune()
	#middle
	color('#9B5A21')
	middune = cursor(0,450,30)
	middune.drawRandDune()
	#close
	color('#D76539')
	frontdune = cursor(0,550,20)
	frontdune.drawRandDune()
def background():
	color('#09B4FA')
	fillRectangle(0,0,1300,700)
def sun():
	color("#FF542A")
	fillCircle(650,275,100)
def tumbleweed(size=20):
	color("brown")
	pensize(1)
	x=randint(0,1300)
	y=randint(350,700)
	for i in range(50):
		drawLine(randint(x-size,x+size),randint(y-size,y+size),randint(x-size,x+size),randint(y-size,y+size))