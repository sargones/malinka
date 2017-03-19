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
        print('\nword is fine')
    else:
        print('\nnot palindrome')
            

pali(input('check a string, if it\'s palindrome :\n')
