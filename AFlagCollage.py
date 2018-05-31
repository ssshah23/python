#Author Name: Shveta Shah
#Lab time: Monday at 10.00 a.m. to 10:45 a.m.
#Date: 11/07/2016
# Description : The purpose of this project is to create a collage pictures to resembles the flag of a country. I draw an Ireland flag.  
# For this project, I received help from the following member of CS 111 : Shruti Shah

# using Posterization method by posterizing a picture into 4 colors with shades of green
def makeGreen(pict):
  # get a list of pixels from the picture
  pixelList = getPixels (pict)
  
  # loop for every pixel in the list
  for pix in pixelList:
    red = getRed (pix)
    green = getGreen (pix)
    blue = getBlue (pix)
    
    # modify the grayAmount from the color at the pixel 
    grayAmount = (red*0.299 + green*0.587 + blue*0.114)
    
    # store the modified color value back into the picture
    if grayAmount <= 63:
      setRed   (pix, 34)
      setGreen (pix, 139)
      setBlue  (pix, 34)
    elif grayAmount <= 127:
      setRed   (pix, 107)
      setGreen (pix, 142)
      setBlue  (pix, 35)
    elif grayAmount <= 191:
      setRed   (pix, 50)
      setGreen (pix, 205)
      setBlue  (pix, 50)
    else:
      setRed   (pix, 173)
      setGreen (pix, 255)
      setBlue  (pix, 50)
      
# using "Make Black and White" method to make black And white picture
def makeBlackandWhite(pict):
  # get a list of pixels from the picture
  pixelList = getPixels(pict)
  
  # loop for every pixel in the List 
  for pix in pixelList:
    # access the color value at that pixel
    red = getRed (pix)
    green = getGreen (pix)
    blue = getBlue (pix)
    
    # modify the color values
    grayAmount = (red*0.299 + green*0.587 + blue*0.114)
    
    # store the modified color value back into the picture
    if grayAmount <= 127:
      setRed   (pix, grayAmount)
      setGreen (pix, grayAmount + 0.2)
      setBlue  (pix, grayAmount + 0.2)
    if grayAmount > 127:
      setRed   (pix, 255)
      setGreen (pix, 255)
      setBlue  (pix, 255)
      
      
# using posterization method give shade of orange color
def makeOrange(pict):
  # get a list of pixels from  the picture
  pixelList = getPixels (pict)
  
  for pix in pixelList:
    red = getRed (pix)
    green = getGreen (pix)
    blue= getBlue (pix)
    
    # modify the color Values
    grayAmount = (red*0.299 + green*0.587 + blue*0.114)
    if (grayAmount < 63):
      # set the pixel to Midnight Blue
      setRed (pix, 255)
      setGreen  (pix, 0)
      setBlue (pix, 0)
    elif(grayAmount < 127 ):
      #set the pixel to slate Blue
      setRed (pix, 255)
      setGreen (pix, 165)
      setBlue (pix, 0)
    elif(grayAmount < 191):
      # set the pixel to Royal Blue
      setRed (pix, 255)
      setGreen (pix,140)
      setBlue (pix, 0)
    else:
      # set the pixel to Light Cyan
      setRed (pix, 255)
      setGreen (pix, 69)
      setBlue (pix, 0)

 
def join ( pict1, pict2, pict3) :
  # get the size for the resulting picture
  width1 = getWidth (pict1)    # the number of columns
  print "The width of the picture 1 is: " + str (width1)
  height1 = getHeight (pict1)  # the number of rows
  print "The height of the picture 1 is: " + str (height1)
  
  width2 = getWidth (pict2)    # the number of columns
  print "The width of the picture 2 is: " + str (width2)
  height2 = getHeight (pict2)  # the number of rows
  print "The height of the picture 2 is: " + str (height2)
  
  width3 = getWidth (pict3)    # the number of columns
  print "The width of the picture 3 is: " + str (width3)
  height3 = getHeight (pict3)  # the number of rows
  print "The height of the picture 3 is: " + str (height3)
  
  # create the final picture
  result = makeEmptyPicture(width1 + width2 + width3, height1)
  
  # loop for only the pixels around the eyes
  for x in range (0,width1):
    for y in range (0,height1):
      pix1 = getPixel (pict1, x, y)     
      c1 = getColor (pix1) 
      
      # perform the needed translation of coordinates
      modX = (0*width1) + x
      modY = y
      
      pix2 = getPixel (result, modX, modY)
      setColor (pix2, c1)
      
  # loop for only the pixels around the eyes
  for x in range (0,width2):
    for y in range (0,height2):
      pix2 = getPixel (pict2, x, y)     
      c2 = getColor (pix2) 
        
      # perform the needed translation of coordinates
      modX = (1*width1) + x
      modY = y
      
      pix3 = getPixel (result, modX, modY)
      setColor (pix3, c2)   
      
  # loop for only the pixels around the eyes
  for x in range (0,width3):
    for y in range (0,height3):
      pix3 = getPixel (pict3, x, y)     
      c3 = getColor (pix3) 
        
      # perform the needed translation of coordinates
      modX = (2*width1)+ x
      modY =  y 
      
      pixR = getPixel (result, modX, modY)
      setColor (pixR, c3) 
                  
  # send the final picture back to the calling function        
  return result
  
def proj3():
   # determine the location of a specific character inside of a string
   pafResult = pickAFile()
   print pafResult
  
   pos1 = pafResult.rfind ( "\\")
   if (pos1 == -1):
     pos1 = pafResult.rfind ( "/")
     
   dirName = pafResult[ 0: pos1+1]
   # Phoenix park is in Dublin 8, Ireland. This area filled with mature trees also known as 'Dublin's playground'.
   fname1 = dirName + "phoenix1.jpg"       
   pict1 = makePicture (fname1)
   
   width1 = getWidth (pict1)    # the number of columns
   height1 = getHeight (pict1)  # the number of rows
  
   makeGreen (pict1)
   
   # determine the location of a specific character inside of a string
   pos2 = pafResult.rfind ( "\\")
   if (pos2 == -1):
     pos2 = pafResult.rfind ( "/")
     
   dirName = pafResult[ 0: pos2+1]
   # Soda bread is traditional Irish food, they used sodium bicarbonate instead of traditional yeast. 
   fname2= dirName + "Irishsodabread.jpg"
   pict2 = makePicture (fname2)
   
   width2 = getWidth (pict2)    # the number of columns
   height2 = getHeight (pict2)  # the number of rows
     
   makeBlackandWhite (pict2)
   
   
   # determine the location of a specific character inside of a string
   pos3 = pafResult.rfind ( "\\")
   if (pos3 == -1):
     pos3 = pafResult.rfind ( "/")
     
   dirName = pafResult[ 0: pos3+1]
   # Botanic Garden are in Dublin, Ireland. This house is famous for restored and planted glasshouses.
   fname3 = dirName + "BotanicGarden4.jpg"
   pict3 = makePicture (fname3)
   
   width3 = getWidth (pict3)    # the number of columns
   height3 = getHeight (pict3)  # the number of rows
    
   makeOrange (pict3) 
   
   resultpict = join( pict1, pict2, pict3)
  
   # display the modified picture
   show (resultpict)
   saveFile = pickAFile ()
   writePictureTo (resultpict, saveFile)