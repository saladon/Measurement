a = 'slim salim slime slimey slim.slim'
def cword(string,word):
    '''Counts given word in given string and return a integer'''
    wordlist = string.split()
    c = 0
    for x in wordlist:
            if word in x:
                    c += 1
    return c 
