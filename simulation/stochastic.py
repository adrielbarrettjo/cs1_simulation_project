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
myimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
     dw.fill(dw.black)
     dw.draw(myimage, (s[i][0], s[i][2]))

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
print("this is m:", m)

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
print("this is s:",s)

## calling elements of the state's:  s[n][m] n is the state number, starting with 0, m
## is the state number if m = 0, the x coordinate if m = 1, the y
## coordinate if m = 2 | s[0][1] is the zero'th state's x element

## Allowing objects to move from state to state
## A random number is generated between 0
## and 100, and is compared to the probability matrix's row for the
## state the object is in, and the object moves to the next state
## according to that comparitive calculation.
initState = 0


def updateState(state, m):
    ## to determine which state the dot moves to next,
    ## create "bins" and then pick one weighted by probabilities
    ## from the transition matrix
    prob = np.random.randint(0,100)
    prob = prob/100 ##makes p a decimal
    CumulProb = m[state,:]
    print ('this is CP:', CumulProb)
    Bin = CumulProb[0,0]
    print("this is Bin:", Bin)
    print("this is p:", prob)
    for i in range(0, numofs):
        if p < Bin:
            print(i)
            state = i
            return state
            break
        else:
            Bin = Bin + CumulProblP[state, i+1]
            print("This is new Bin", Bin)
    h+=1

################################################################

## Terminates the simulation when the animation has run a h times
def endState(state):
     if h == runtime:
        return True
     else:
        return False

## Run the simulation/ change state no more than once per second
frameRate = 1
initState = 0
## Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
