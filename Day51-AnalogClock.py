import turtle as t
import time
import datetime

t.title('Analog Clock')

t.speed(0)

t.ht()

screen = t.getscreen()

# size of the clock
scale = 3

#face of the clock
t.dot(130*scale)
t.color('white')
t.dot(128*scale)
t.color('black')

# Minute markers
t.home()
for x in range(60):
    t.pu()
    t.fd(60 * scale)
    t.pd()
    t.dot(1 * scale)
    t.pu()
    t.setposition(0,0)
    t.pd()
    t.rt(6)

# Hour markers
t.home()
for x in range(12):
    t.pu()
    t.fd(60 * scale)
    t.pd()
    t.dot(3 * scale)
    t.color('white')
    t.dot(3 * scale * 0.7)
    t.color('black')
    t.pu()
    t.setposition(0,0)
    t.pd()
    t.rt(30)

# shapes for each turtle (graphics)
screen.register_shape("mH", ((-2 * scale, 0 * scale), (-2 * scale, 50 * scale), (0 * scale, 55 * scale),
                             (2 * scale, 50 * scale), (2 * scale, 0* scale)))
screen.register_shape("hH", ((-3 * scale, 0 * scale), (-3 * scale, 35 * scale), (0 * scale, 40 * scale),
                             (3 * scale, 35 * scale), (3 * scale, 0 * scale)))
screen.register_shape("sH", ((-2 * scale, 0 * scale), (0 * scale, 55 * scale), (2 * scale, 0 * scale)))

# sets the time
now = datetime.datetime.now()
second = int(now.strftime("%S"))
minute = int(now.strftime("%M"))
hour = int(now.strftime("%H"))

# adding multiple turtles and setting their shapes
s = t.Turtle()
m = t.Turtle()
h = t.Turtle()
s.shape("sH")
m.shape("mH")
h.shape("hH")

# the dot in the center of the clock
t.dot(4 * scale)

# sets initial heading of the turtles
s.seth(90)
m.seth(90)
h.seth(90)
s.rt(second * 6)
s.rt(minute * 6)
h.rt(hour * 30)

while True:
    time.sleep(1)
    s.rt(6)
    second += 1

    if second == 60:
        second = 0
        minute += 1
        m.rt(6)
    if minute == 60:
        minute = 0
        hour += 1
        h.rt(30)
