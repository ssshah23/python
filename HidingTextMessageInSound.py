# Author: Shveta Shah
# CS111: Monday 10:00-10:50
# Date: 12/01
# A sample python program to use steganography technique to embed and extract a text message in a sound

def main():
  #ask user to enter integer value
  uEnter = requestIntegerInRange ("Enter 1 to embed and Enter 2 to decode hidden message", 1, 2)
  print "The user entered: " + str (value)
  
  if (uEnter == 1):
    embed ()
    
  if (uEnter == 2):
    extract ()

def embed():
  #pick a file from folder
  fname = pickAFile()
  s1 = makeSound (fname)
  length = getLength (s1)
  
  #request user to enter a message
  str = requestString ('Enter a text you want to embed')
  #length of the given string
  length = len(str)
  List = []
  
  # get a samplem List from the sound and the total number of samples
  sampleList = getSamples (s1)
  
  for i in range (0, length):
    #access the sample from position i in the sample LIST
    sample = sampleList [i]
    #get the amplitude value at the sample 
    value = getSampleValue (sample)
    remainder = value % 128
    modValue = value - remainder
    setSampleValue (sample, modValue)
    
  for w in range (length):
    ch = str [w]
    #take the decimal ascii value of a entered message
    asciiNum = ord (ch)
    sample2 = sampleList [w]
    smoothedValue = getSampleValue (sample2)
    finalValue = smoothedValue + asciiNum
    setSampleValue (sample2, finalValue)
  # save open file 
  saveFile = pickAFile()
  writeSoundTo (s1, saveFile)

def extract():
  #open embed save file
  fname = pickAFile ()
  s2 = makeSound (fname)
  
  # get a samplem List from the sound and the total number of samples
  sampleList = getSamples (s2)
  lengthSound = getLength (s2)
  message = " "
  
  #loop for all samples in the sound
  for i in range (0, lengthSound):
    sample = sampleList [i]
    ampValue = getSampleValue (sample)
    #smoothed the open sound file
    lsvalue = ampValue % 128
    ch2 = chr(lsvalue)
    message = message +ch2
    
    if lsvalue == 0:
      #extract embed message
      showInformation (message)
      return
  

    
  
  
  