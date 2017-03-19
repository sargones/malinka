from time import sleep, time
from random import randint

l = []
m = 0

def game():
    t = 0
    while str.lower(input('Do you want to check your reaction? ')) in ('y', 'yes'):
        sleep(randint(1, 10))
        start = time()
        print('Press Enter key now!')
        input()
        reaction_time = '% .3f' % (time() - start)
        print('It took', reaction_time, 'seconds to press the key :)')
        print('Well done.')
        l.append(reaction_time)
        l.sort()
        #print(l)
        m = ('|Best result so far is' + str(float(l[0])) + 'seconds!|')
        print('='*(len(m ) + 2))
        print('|Best result so far is', float(l[0]) , 'seconds!|')
        print('='*(len(m) + 2))
        t = t +1
    return t
        
t = game()
print('\nThanks for playing with Python!')
print('Best score out of', t, 'attempts:', l[0],'sec\n')



