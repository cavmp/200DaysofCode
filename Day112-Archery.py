import turtle
import random
from math import sqrt

def drawCircle(pen, colorFill, size, x, y):
  pen.penup()
  pen.color(colorFill)
  pen.fillcolor(colorFill)
  pen.goto(x,y)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
  pen.pendown()
    
def drawTarget(pen):
  drawCircle(pen, "#00000", 152, 0,-152)
  drawCircle(pen, "#FFFFFF", 150, 0,-150)
  drawCircle(pen, "#000000", 120, 0,-120)
  drawCircle(pen, "#33AAFF", 90, 0,-90)
  drawCircle(pen, "#FF0000", 60, 0,-60)
  drawCircle(pen, "#FFFF00", 30, 0,-30)

def drawCross(pen, color, size, x, y):
  pen.pensize(3)
  pen.color(color)
  pen.penup()
  pen.goto(x-size,y-size)
  pen.pendown()
  pen.goto(x+size,y+size)
  pen.penup()
  pen.goto(x-size,y+size)
  pen.pendown()
  pen.goto(x+size,y-size)

def writeScore(pen, text):
  pen.penup()
  pen.goto(-80, 170)
  pen.color("#000000")
  pen.write(text, None, None, "16pt bold")

def calculateScore(arrowx,arrowy):
  score = 0
  distance = 0
  #Pythagoras formula to calculate the distance to the centre.
  distance = sqrt((arrowx * arrowx) + (arrowy * arrowy))
  
  if distance > 0 and distance < 30:
    score += 10
  if distance > 31 and distance < 60:
    score += 5
  if distance > 61 and distance < 90:
    score += 3
  if distance > 91 and distance < 120:
    score += 2
  if distance > 121 and distance < 150:
    score += 1
  if distance > 150:
    score += 0

  return score
  
    
#Main Program Starts Here
myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.shape("arrow")

drawTarget(myPen)

#Shooting the arrow
arrowx= random.randint(-150,150)
arrowy= random.randint(-150,150)
drawCross(myPen,"#FF7777",10,arrowx,arrowy)

#Calculate and display score
score = calculateScore(arrowx,arrowy)
writeScore(myPen,"Your Score: + " + str(score))

#Hide the pen
myPen.penup()
myPen.goto(-300,-300)

myPen.getscreen().update()	
