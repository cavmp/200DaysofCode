import turtle
import random
import math
from math import sqrt

def drawLayer(radius, color1, color2):
  angle = 18
  initialAngle=angle
  myPen.penup()
  myPen.setheading(180)
  myPen.goto(0,radius)
  myPen.circle(radius, angle//2) #move along arc
  myPen.pendown()
  i=0

  while i <= 20 :
    myPen.begin_fill()
    myPen.circle(radius, angle) #move along arc
    myPen.left(90)
    myPen.forward(radius) # turtle now at centre
    myPen.left(180-initialAngle)
    myPen.forward(radius) # back on edge of circle
    myPen.left(90)
    myPen.speed(0)
    angle = initialAngle*2 # moves turtle to begin next pie shape
    i = i + 1 
    if i %2 == 0 :
         myPen.fillcolor(color1)    # this conditional creates the alernating pattern
    else :
         myPen.fillcolor(color2)
    myPen.end_fill()

def drawTarget():    
  drawLayer(144,"#FF0000","#099909")
  drawLayer(134,"#111111","#FFFFAA")
  drawLayer(84,"#FF0000","#099909")
  drawLayer(74,"#111111","#FFFFAA")

  #Outer Bull
  myPen.fillcolor("#099909")
  myPen.penup()
  myPen.setheading(180)
  myPen.goto(0,20)
  myPen.begin_fill()
  myPen.pendown()
  myPen.circle(20)
  myPen.end_fill()
  
  #Bull's Eye
  myPen.fillcolor("#FF0000")
  myPen.penup()
  myPen.setheading(180)
  myPen.goto(0,10)
  myPen.begin_fill()
  myPen.pendown()
  myPen.circle(10)
  myPen.end_fill()

def drawCross(color, size, x, y):
  myPen.pensize(3)
  myPen.color(color)
  myPen.penup()
  myPen.goto(x-size,y-size)
  myPen.pendown()
  myPen.goto(x+size,y+size)
  myPen.penup()
  myPen.goto(x-size,y+size)
  myPen.pendown()
  myPen.goto(x+size,y-size)

def writeScore(text):
  myPen.penup()
  myPen.goto(-80, 170)
  myPen.color("#000000")
  myPen.write(text, None, None, "16pt bold")

def calculateScore(arrowx,arrowy):
  score = 0
  distance = sqrt((arrowx * arrowx) + (arrowy * arrowy))
  
  #Use SOCATOA to calculate the angle matching the arrow position
  angle = math.degrees(math.atan2(arrowy,arrowx))
  if angle > 0 and angle < 10: 
    score += 6
  if angle > 9 and angle < 28: 
    score += 13
  if angle > 27 and angle < 46:
      score += 4
  if angle > 45 and angle < 64:
      score += 18
  if angle > 63 and angle < 82:
    score += 1
  if angle > 81 and angle < 100:
    score += 20
  if angle > 99 and angle < 118:
    score += 5
  if angle > 117 and angle < 136:
    score += 12
  if angle > 135 and angle < 154:
    score += 9
  if angle > 153 and angle < 172:
    score += 14
  if angle > 171 and angle < -170:
    score += 11
  if angle > -171 and angle < -152:
    score += 8
  if angle > -153 and angle < -134:
    score += 16
  if angle > -135 and angle < -116:
    score += 7
  if angle > -117 and angle < -98:
    score += 19
  if angle > -99 and angle < -80:
    score += 3
  if angle > -81 and angle < -62:
    score += 17
  if angle > -63 and angle < -44:
    score += 2
  if angle > -45 and angle < -26:
    score += 15
  if angle > -27 and angle < -8:
    score += 10
  if angle > -9 and angle < 0:
    score += 6

  print(angle) 
  
  if distance > 0 and distance < 11: 
    score += 50
  if distance > 10 and distance < 21: 
    score += 25
  if distance > 20 and distance < 75:
    score *= 1
  if distance > 74 and distance < 85:
    score *= 3
  if distance > 84 and distance < 134:
    score *= 1
  if distance > 134 and distance < 145:
    score *= 3
  if distance > 146:
    score *= 0 
  
  return score

##########################################
#        MAIN PROGRAM STARTS HERE        #
##########################################
myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.color("#FF0000")

myPen.shape('arrow')
myPen.pensize(1)
myPen.pencolor('black')

drawTarget()
#Shooting the arrow
arrowx= random.randint(-150,150)
arrowy= random.randint(-150,150)
drawCross("#00FFFF",10,arrowx,arrowy)

#Calculate and display score
score = calculateScore(arrowx,arrowy)
writeScore("Your Score: + " + str(score))

#Hide the pen
myPen.penup()
myPen.goto(-300,-300)

myPen.getscreen().update()
