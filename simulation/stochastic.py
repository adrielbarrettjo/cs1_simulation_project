# stochastic.py
import random as randint
import numpy as np
import runWorld as rw
import drawWorld as dw
import pygame as pg

## Initialize world

## 1| Initializing Display
name = "RPG: Random Path Generator"
width = 500
height = 500
rw.newDisplay(width, height, name)


## 2| Defining the number of states and generating a random
## transition matrix for those states

## 2.1| Number of States
numofs = 8

## 2.2| Transition Matrix
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
## print("this is m:", m)

## 3| Creating the States

## 3.1| States are created in the array s represented by a (x,y) pair
s = []
q=0
while q < numofs:
    sx = np.random.randint(0, width)
    sy = np.random.randint(0, height)
    state = (sx, sy)
    s.append(state)
    q += 1
## print("this is s:",s)

## 3.2| The following s array is for demonstration purposes, it makes a
## grid of states instead of random states so that pepole can more
## easily understand what a state is. Comment this line out to return
## to randomly generated states. Using this set of states requires
## numofs = 8
## s = [(100,166),(200,166),(300,166),(400,166),(100,333),(200,333),(300,333),(400,333)]


################################################################

## To determine which state the dot moves to next,
## create "bins" and then pick one weighted by probabilities
## from the transition matrix

## The various print commands are to make sure the program is
## calculating the probabilities and bins correctly


def updateState(state):
    prob = np.random.randint(0,100)
    prob = prob/100 ##makes p a decimal
    CumulProb = m[state,:]
    Bin = CumulProb[0,0]
##    print ('this is CP:', CumulProb)
##    print("this is Bin:", Bin)
##    print("this is p:", prob)
    for i in range(0, numofs-1):
        if prob < Bin:
            print("The state is:", i)
            state = i
            break
        else:
##            print("this is Bin2", Bin)
##            print("this is CP2", CumulProb[0, (i+1)])
            Bin = Bin + CumulProb[0, (i+1)]
##            print("This is new Bin", Bin)
    return(state)

################################################################

## Display the state by drawing the image at the current state's (x,y)
## pair

myimage = dw.loadImage("dog.jpg")

def updateDisplay(state):
     dw.fill(dw.black)
     dw.draw(myimage, (s[state][0], s[state][1]))


################################################################

## Terminates the simulation when the state is a given number

def endState(state):
     if state == 4:
        return True
     else:
        return False


################################################################

## A blank handle event for possible extension of the simulation

def handleEvent(state, event):
    return(state)


################################################################

## Change state no more than once per second
frameRate = 1

## Starting position is the 0 state
initState = 0


################################################################

## Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
