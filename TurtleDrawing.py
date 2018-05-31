#Project 1: In this project, use the turtle class to draw a large multifaceted geometrical shape onto a picture. These modification are to add something to the image. Normally this would be to draw something in the foreground of an image that is just a scene.
#Author: Shveta Shah
#Date: 9/25/2016
#CS 111


#to draw a rectangular
def rectangular(t):
  for i in range(2):         #repeat following code 2 times
    forward(t,50)
    turn(t,90)
    forward(t,70)
    turn(t,90)
    
#to draw a circle
def drawCircle(t):
  for i in range(8):        # repeat following code 8 times to draw a circle
    forward(t,10)
    turn(t,45)
    
#to draw a triangle                 
def triangle (t2):
  numSide = 120
  for i in range(numSide/40):             #repeat following code 3 times 
    turn(t2,numSide)                      # need 3 sides
    forward(t2,numSide/12)                #turn 120/12 = 10
 
def square(t2):
  for i in range(4):     #repeat following code 2 times
    turn(t2,90)
    forward(t2,10)  	 
    
def hexagonal(t):             
  for i in range(6):    #repeat following code 6 times
    turn(t, 60)             # turn 60 degree
    forward(t, 40)
    
def proj1():
  #save a picture to the operating system
  saveFileName = pickAFile()
  pict = makePicture(saveFileName)
  t = makeTurtle(pict)
  writePictureTo (pict, saveFileName)
  t.setPenWidth(3)
  #rectangular face
  t.setPenColor (yellow)
  rectangular(t)
  
  #move pen to draw circles with same pen width and pen color
  penUp(t)
  forward(t,50)
  penDown(t)
  turn(t,-130)
  t.setPenWidth(3)
  drawCircle(t)
  
  #move turtle to the left to draw a second circle
  penUp(t)
  backward(t,10)
  turn(t,-135)
  forward(t,60)
  turn(t,40)
  penDown(t)
  turn(t,-130)
  drawCircle(t)
 
  #make a new turtle for other face parts
  t2 = makeTurtle(pict)
  
  #set pen width and color for different shapes
  t2.setPenWidth(2)
  t2.setPenColor(red)
  penUp(t2)
  turn(t2, 50)
  forward(t2, 40)
  turn(t2,40)
  penDown(t2)
  turn(t2, 180)
  triangle (t2)
  
  #move t2 and change color to black to draw square triangle
  t2.setPenColor(black)
  penUp(t2)
  turn(t2,45)
  forward(t2, 25)
  turn(t2, 45)
  penDown(t2)
  square(t2)
  
  penUp(t2)
  turn(t2, 90)
  forward(t2, 35)
  turn(t2, -90)
  penDown(t2)
  square(t2)
  turn(t2, 180)
  
  turn(t, 180)
  penUp(t)
  forward(t, 53)
  turnRight(t)
  forward(t, 10)
  penDown(t)
  
  #change pen color and move turtle to draw other shape
  t.setPenColor(blue)
  turn(t, -90)
  forward(t, 5)
  turn(t, 85)
  forward(t, 40)
  turn(t, 90)
  forward(t, 5)
  turn(t, 180)
  penUp(t)
  forward(t,5)
  penDown(t)
  
  #make color to draw hexagonal 
  turn(t,210)
  myOrange = makeColor(220,0,220)
  t.setPenColor (myOrange) 
  hexagonal(t)
  
  penUp(t)
  turn(t,180)
  forward(t,15)
  turn(t,90)
  penDown(t)
  forward(t,10)
  turn(t,-90)
  forward(t,30)
  turn(t,-60)
  forward(t,20)
  turn(t,-90)
  forward(t,10)
  #use previous color combination to draw right hand
  t2.setPenColor(myOrange)
  penUp(t2)
  turn(t2,-45)
  forward(t2,15)
  turn(t2,45)
  forward(t2,47)
  penDown(t2)
  turn(t2,-110)
  forward(t2,10)
  turn(t2,-90)
  forward(t2,30)
  turn(t2,-60)
  forward(t2,20)
  turn(t2,-90)
  forward(t2,10)
  turn(t2,-90)
  forward(t2,15)
  turn(t2,60)
  forward(t2, 21)
  #move t2 to draw legs, set penwidth and blue color
  sizeLegs = 45
  myPent = makeColor(0,0,200)
  t2.setPenColor(myPent)
  t2.setPenWidth(3)
  penUp(t2)
  turn(t2,43)
  forward(t2, 65)
  turn(t2, -20)
  forward(t2,2)
  penDown(t2)
  forward(t2,sizeLegs)
  turn(t2,-90)
  forward(t2, 15)
  turn(t2, -90)
  forward(t2,sizeLegs)
  penUp(t2)
  turn(t2, -90)
  forward(t2,35)
  turn(t2,-90)
  penDown(t2)
  forward(t2, sizeLegs) 
  turn(t2, -90)
  forward(t2,15)
  turn(t2,-90)
  forward(t2,sizeLegs)
  
  penUp(t2)
  forward(t2,25)
  penDown(t2)
  
  #move turtle to the left 150 pixels 
  penUp(t)
  turn(t,160)
  forward(t, 150)
  penDown(t)
  #make different color by changing the amount of red and green
  myBlue = makeColor(820,100,0)
  t.setPenColor (myBlue)
  t.setPenWidth(25)
  for i in range (30):
    forward(t,3)
    turn(t,360/30)
  #show the picture to make it visible  
  show (pict)
  
  
  
 
 



