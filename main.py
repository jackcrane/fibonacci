#Draw the Fibonacci Spiral using Turtle Graphics


from turtle import *

import turtle
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("*********************************************************************\nFibonacci visualization\nCreated by Jack Crane\n\n*********************************************************************\n\n\n")


fibo_nr = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]  #Fibonacci numbers this could be calculated instead

print("Please answer the following questions. They cannot be left blank\nI reccomend 16 for the first question, and 1 for the second")

loopcount = int(raw_input("\nHow many iterations? (max 16): "))

if loopcount>15:
    loopcount = 15

factor = input("\nZoom Factor (Base should be 1): ")                        #Enlargement factor
print("\n*********************************************************************\nNow calculating... Press control+c to interrupt.")

def draw_square(side_length):  #Function for drawing a square
    for i in range(4):
        forward(side_length)
        right(90)

nr_squares=len(fibo_nr)


penup()
goto(90,70)                  #Move starting point right and up
pendown()
# Was previously nr_squares
for i in range(loopcount):
    draw_square(factor*fibo_nr[i]) #Draw square
    penup()                        #Move to new corner as starting point
    forward(factor*fibo_nr[i])
    right(90)
    forward(factor*fibo_nr[i])
    pendown()
    print(fibo_nr[i])
        
penup()
goto(90,70)       #Move to starting point
setheading(0)   #Face the turtle to the right
pencolor('red')
pensize(3)
pendown()


#Draw quartercircles with fibonacci numbers as radius
# Was previously nr_squares
for i in range(loopcount):
    circle(-factor*fibo_nr[i],90)  # minus sign to draw clockwise

turtle.done()