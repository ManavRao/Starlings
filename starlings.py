from vpython  import *
import random
import time
import math

birds = []
nbirds = 2

class BirdClass():
	def __init__(self):
		self.value = sphere(pos = vector(random.randint(-30,30),random.randint(-30,30),random.randint(-30,30)), radius = 1.0)
		self.velocity = vector(0,0,0)

for i in range(0,nbirds):
	birds.append(BirdClass())
	if (i%3==0):
		birds[i].value.color = color.red
	if (i%3==1):
		birds[i].value.color = color.cyan
 
def rule1(bird):
	pc = vector(0,0,0)
	for obirds in birds:
		pc = pc + obirds.value.pos
	pc = pc - bird.value.pos
	pc = pc/((nbirds-1)*1.0)
	return ((pc - bird.value.pos)/100.0)

def rule2(bird):
	c = vector(0,0,0)
	for obirds in birds:
		a = (obirds.value.pos)
		b = (bird.value.pos)
		if (math.sqrt(dot(a,a) + dot(b,b) - 2*dot(a,b))<100):
			c = c - a + b
	
	return c

def rule3(bird):
	pv = vector(0,0,0)
	for obirds in birds:
		pv = pv + obirds.velocity
	pv = pv - bird.velocity
	pv = pv/((nbirds-1)*1.0)
	return (pv - bird.velocity)/8.0

def rule4(bird):
	xmin = -30
	xmax = 30
	ymin = -30
	ymax = 30
	zmin = -30
	zmax = 30
	v = vector(0,0,0)
	
	if bird.value.pos.x < xmin:
		v.x = 15
	if bird.value.pos.x > xmax:
		v.x = -15
	if bird.value.pos.y < ymin:
		v.y = 15
	if bird.value.pos.y > ymax:
		v.y = -15
	if bird.value.pos.z < zmin:
		v.z = 15
	if bird.value.pos.z > zmax:
		v.z = -15
	return v

def limit_velocity(bird):
	vlim = 30
	if (math.sqrt(dot(bird.velocity,bird.velocity)) > vlim):
		bird.velocity = ((bird.velocity)*vlim)/math.sqrt(dot(bird.velocity,bird.velocity))
	
def move_birds():
	for bird in birds:
		v1 = rule1(bird)
		#print (v1)
		v2 = rule2(bird)
		#print (v2)
		v3 = rule3(bird)
		#print (v3)
		v4 = rule4(bird)

		bird.velocity = bird.velocity + v1 + v2 + v3
		#print(bird.velocity) 
		limit_velocity(bird)
		current = bird.value.pos 
		final = bird.value.pos + bird.velocity + v4

		while((abs(current.x - final.x) > 1) or (abs(current.y - final.y) > 1) or (abs(current.z - final.z) > 1)):
			if (current.x>final.x):
				current.x = current.x - 1
			if (current.x<final.x):
				current.x = current.x + 1
			if (current.y>final.y):
				current.y = current.y - 1
			if (current.y<final.y):
				current.y = current.y + 1
			if (current.z>final.z):
				current.z = current.z - 1
			if (current.z<final.z):
				current.z = current.z + 1
			bird.value.pos = current


		#print(bird.value.pos)
		#print ("-------------------")
while(1):
	
	#time.sleep(.500)
	move_birds()
