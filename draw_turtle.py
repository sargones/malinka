'''
#using function inside function

def full_song(x):
    for i in range (x):
        song(m)

#full_song()

def song(s):
    print(s)

m = str(input('give me text for multipying: '))
full_song(int(input('how many times: ')))
'''

import turtle
turtle.st()
turtle.speed(1)
turtle.shape('classic')
turtle.delay = 2


def make_circle():
    m = 3
    for p in range(120):
        turtle.left(3)
        turtle.forward(m)
        if p > 60:
            turtle.st()
            turtle.shape('turtle')
    turtle.ht()

def make_smaller_square():
    ''' This is a test for a document.
that should be used for make_smaller_square'''
    m = 200
    for p in range(22):
        turtle.left(90)
        turtle.forward(m)
        m -= 10
    turtle.ht()



#turtle.speed(8)
make_smaller_square()

turtle.penup()
turtle.backward(90)
turtle.right(90)
turtle.backward(100)
turtle.left(90)
turtle.pendown()

make_circle()
