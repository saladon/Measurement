def cword(string,word):
    '''Counts given word in given string and return a integer'''
    wordlist = string.split()
    c = 0
    for x in wordlist:
            if x == word:
                    c += 1
    if c == 0:
            c = 'Word not in text'
    return c 
