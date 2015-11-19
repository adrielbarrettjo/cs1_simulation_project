# stochastic.py
import random as randint
import numpy as np
import runWorld as rw
import drawWorld as dw
import pygame as pg

## Initialize world
## name = "RPG: Random Path Generator"
width = 500
height = 500
## rw.newDisplay(width, height, name)
## number of states 
numofs = 6
## number of times the object walks
runtime = 10

################################################################

## Display the state by drawing the image at the current state's (x,y)
## pair
## myimage = dw.loadImage("image.bmp")
## def updateDisplay(state):
##     dw.fill(dw.black)
##     dw.draw(myimage, (state[1], state[2]))

################################################################

## generate random 6x6 stochastic matrix
i = 0
m = []
while i < numofs:
    t = 0
    a = []
    while t < numofs:
        v = [np.random.randint(0,100)]
        a.extend(v)
        t += 1
    s = np.sum(a)
    a = a/s
    m.append(a)
    i += 1
m = np.matrix(m)
print("this is m", m)

## Creating the states
## States take the form (the state's number, the x coordinate, the y
## coordinate), while s is the array containing all the states
s = []
q=0
while q < numofs:
    sx = np.random.randint(0, width)
    sy = np.random.randint(0, height)
    state = (sx, sy)
    s.append(state)
    q += 1
print("this is s",s)

## calling elements of the state's:  s[n][m] n is the state number, starting with 0, m
## is the state number if m = 0, the x coordinate if m = 1, the y
## coordinate if m = 2 | s[0][1] is the zero'th state's x element

## Allowing objects to move from state to state
## A random number is generated between 0
## and 100, and is compared to the probability matrix's row for the
## state the object is in, and the object moves to the next state
## according to that comparitive calculation.
initState = 0


## def updateState(state, m)
p = np.random.randint(0,100) 
p = p/100 ##makes p a decimal
CP = m[state,:]
Bin = CP[0]
for i = 0 to numofs:
    if p < Bin:
        print(i)
        return i
    else:
        Bin = Bin + CP[i+1]
        i += 1


################################################################

## Terminates the simulation when the animation has run a h times
## def endState(state):
##     if h == runtime:
##         return True
##     else:
##         return False

## Run the simulation no faster than 60 frames per second
frameRate = 60

## Run the simulation!
## rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
