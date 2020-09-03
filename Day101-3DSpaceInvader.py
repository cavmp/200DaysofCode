from vpython import *

pixels   =   [[0,0,1,0,0,0,0,0,1,0,0]]
pixels.append([0,0,0,1,0,0,0,1,0,0,0])
pixels.append([0,0,1,1,1,1,1,1,1,0,0])
pixels.append([0,1,1,0,1,1,1,0,1,1,0])
pixels.append([1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,0,1,1,1,1,1,1,1,0,1])
pixels.append([1,0,1,0,0,0,0,0,1,0,1])
pixels.append([0,0,0,1,1,0,1,1,0,0,0])

cubes = []
#Create all cubes/pixels of our space invader
for row in range(0,len(pixels)):
  for col in range(0,len(pixels[row])):
    pixel=pixels[row][col]
    if pixel>0:
      cube = box(color=vector(0.6,0,0.6), pos=vector(col,-row,0), length=1, height=1, width=1, opacity=1)
      cubes.append(cube)
invader = compound(cubes)

theta=0.1
framerate=20
#Translate our invader to the center of the screen
invader.pos = invader.pos + vector(-6,6,0)

#Animate our space invader
while True:
  rate(framerate)
  invader.rotate(angle=theta, axis=vector(1,1,1), origin=vector(0,0,0))
