##Project 2: In this project, combine two images into a single 3 dimension images. These images will be viewed using red/blue glasses to give the 3D effect. The final image will attempt to be a grayscale of the object in the original images.
#Author: Shvetaben Shah
#Lab time: Monday at 10a.m.
#Date: 10/20/2016

def proj2():
  # pick up a file 
  openFileName = pickAFile()      
  #get the picture information    
  pict1 = makePicture (openFileName)   
  pixelList = getPixels (pict1)
  #get the width and height of the picture
  width1 = getWidth (pict1)
  height1 = getHeight (pict1)
  
  
  # create the final picture
  pict3 = makeEmptyPicture(width1, height1)
  finalPixelList = getPixels (pict3)
  #set red color for first image
  for pix in pixelList:
    red= getRed(pix)
    green = getGreen(pix)
    blue = getBlue (pix)
    redAmount = (red*0.299 + green*0.587 + blue*0.114)
    setRed(pix, redAmount)
    setGreen(pix, 0)
    setBlue(pix,0)
  show (pict1)
  
  openFileName2 = pickAFile()          # ask the user to specify a picture
  pict2 = makePicture (openFileName2)   # get the picture information into JES
  pixelList2 = getPixels(pict2)
  
  width2 = getWidth(pict2)
  height2 = getHeight(pict2)
  # set cyan color for second image
  for pix in pixelList2:
    red2 = getRed (pix)
    green2 = getGreen(pix)
    blue2 = getBlue (pix)
    cyanAmount = (red2*0.299 + green2*0.587 + blue2*0.114)
    setRed(pix, 0)
    setGreen(pix, cyanAmount)
    setBlue(pix, cyanAmount)
    
    
  show(pict2)
  #compare height and width of both pics 
  if(width1 == width2 and height1 == height2):
    # loop for only the pixels 
    for x in range (width1):
      for y in range (height1):
        pix1 = getPixel (pict1, x, y)
        pix2 = getPixel (pict2, x, y)
        pix3 = getPixel (pict3, x, y)
      
        r1 = getRed (pix1)
        g1 = getGreen (pix1)
        b1 = getBlue (pix1)
      
        r2 = getRed (pix2)
        g2 = getGreen (pix2)
        b2 = getBlue (pix2)
        
        #set color for final picture
        r3 = (r1) 
        g3 = (g2) 
        b3 = (b2) 
      
        setRed (pix3, r3)
        setGreen (pix3, g3)
        setBlue (pix3, b3)
  else :
      #create error command 
      print "Error: pictures have different heights and widths. Please try to again with same heights and widths."
      quit()
   #display modified picture   
  show(pict3)
  saveFile = pickAFile()
  writePictureTo(pict3, saveFile)