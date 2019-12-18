#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Skylar Strieper
#Date
#12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries


#create turtle
import turtle as trtl
sketch = trtl.Turtle()

#movement functions
def up():
    sketch.setheading(90)
    sketch.forward(10)

def down():
    sketch.setheading(270)
    sketch.forward(10)    

def right():
    sketch.setheading(0)
    sketch.forward(10)

def left():
    sketch.setheading(180)
    sketch.forward(10)

def space():
    sketch.clear()


#color/drawing functions
def o():
    sketch.pensize(1)
def p():
    sketch.pensize(2)


#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(sketch.pensize(1), "o")
wn.onkeypress(sketch.pensize(2), "p")
wn.onkeypress(sketch.clear, "space")
#listen
wn.listen()

wn.mainloop()
#mainloop
