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

'''
Draw a turtle shapes

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
   \''' This is a test for a document.
that should be used for make_smaller_square\'''
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
'''

'''
def countdown(n, s):
    if n <= 0:
        return
    else:
        print(s)
        countdown(n-1, s)
        

countdown(int(input('number: ')), input('text:'))
'''


'''def fori(a, b, c, n):
    if a**n + b**n ==c**n:
        print('yes')
    else:
        print('no')

fori(4, 4, 6, 3)
'''
'''
def compar(x, y, z):
    print ((x < y) and (y < z))

    
compar(3, 5, 6)	    
'''


'''
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

fibonacci(5)
'''

'''
#if word is palindrome is a word that is
#spelled the same backward and forward, like moon

def pali(word):
    word1 = str(word).replace(' ', '')
    l = len(word1)
    k = 0
    if l <3:
        print('Word should be at least 3 characters!')
    else:
       for n in range(l):
            if word1[n] == word1[((n+1)*(-1))]:
                k += 1
            
    if k == l:
        print('word is fine')
    else:
        print('not palindrome')
            

pali(input('check a string, if it\'s palindrome :\n'))
'''
'''
initial = ['a', 'b', 'c', 'd', 'five']
g = iter(initial)

while True:
    try:
        i = 0
        for i  in range(5):
            print(next(g))
            i += 1
    except: StopIteration
    print('done')
    break
'''

'''
write string in opposite direction

st = 'Plamen'
i = 1

ss = (1, 2, 3, 4, 5)

while i < (len(st) + 1):
    print(st[i*(-1)])
    i = i +1

'''

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    #return -1

#print(find('Plamen', 'l'))

st = str(input('String to be onverted: '))
new_st = st.upper()
print (new_st)
print((new_st.lower()))

