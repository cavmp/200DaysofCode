from vpython import *

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

GREEN_OFF = vector(0,0.5,0)
GREEN_ON = vector(0,1,0)
AMBER_OFF = vector(0.5,0.3,0)
AMBER_ON = vector(1,0.6,0)
RED_OFF = vector(0.5,0,0)
RED_ON = vector(1,0,0)

#First Traffic Light
frame_1 = box(color=vector(0.3,0.3,0.3), pos=vector(-5,4,0), length=4, height=10, width=4, opacity=1)
pole_1=cylinder(color=vector(0.3,0.3,0.3), pos=vector(-5,-6,0), axis=vector(0,14,0), radius=1)
redBulb_1 = sphere(color=RED_OFF, pos=vector(-5,7,2), radius=1.4)
amberBulb_1 = sphere(color=AMBER_OFF, pos=vector(-5,4,2), radius=1.4)
greenBulb_1 = sphere(color=GREEN_OFF, pos=vector(-5,1,2), radius=1.4)

#Second Traffic Light
frame_2 = box(color=vector(0.3,0.3,0.3), pos=vector(5,4,0), length=4, height=10, width=4, opacity=1)
pole_2=cylinder(color=vector(0.3,0.3,0.3), pos=vector(5,-6,0), axis=vector(0,14,0), radius=1)
redBulb_2 = sphere(color=RED_OFF, pos=vector(6.6,7,0), radius=1.4)
amberBulb_2 = sphere(color=AMBER_OFF, pos=vector(6.6,4,0), radius=1.4)
greenBulb_2 = sphere(color=GREEN_OFF, pos=vector(6.6,1,0), radius=1.4)


framerate=15
frame=0

while True:
  frame+=1
  if frame<=50:
    redBulb_1.color = RED_ON
    amberBulb_1.color = AMBER_OFF
    greenBulb_1.color = GREEN_OFF
  elif frame<=70:
    redBulb_1.color = RED_ON
    amberBulb_1.color = AMBER_ON
    greenBulb_1.color = GREEN_OFF
  elif frame<=120:
    redBulb_1.color = RED_OFF
    amberBulb_1.color = AMBER_OFF
    greenBulb_1.color = GREEN_ON
  elif frame<=140:
    redBulb_1.color = RED_OFF
    amberBulb_1.color = AMBER_ON
    greenBulb_1.color = GREEN_OFF
  elif frame>120:
    frame=0
  rate(framerate)
