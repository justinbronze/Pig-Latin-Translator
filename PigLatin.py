print('Welcome to the Pig Latin Translator. Input your word or phrase below.')
sent = (input("Word or Phrase to be translated: "))

sentlist1 = sent.strip('.').strip('?').strip('!').split(' ')
nonletter = 0
for w in sentlist1:
    if w.isalpha() == False:
        nonletter +=1
sentlist = sent.strip('.').split(' ')
if len(sent) > 0 and (nonletter == 0): 
    psent = ''
    if len(sentlist) == 1:
        for word in sentlist:
            wordpl = (word[1].upper() + word[2:] + word[0].lower() + ('ay'))
    if len(sentlist) == 2:
        for word in sentlist:
            if word == sentlist[0]:
                wordpl = (word[1].upper() + word[2:] + word[0].lower() + ('ay') + ' ')
            else:
                wordpl = (word[1].upper() + word[2:] + word[0].lower() + ('ay'))
            psent += wordpl
    else:    
        for word in sentlist:
            if word == sentlist[0]:
                if len(word) == 1:
                    wordpl = (word[0].upper() + ('ay') + ' ')
                else:
                    wordpl = (word[1].upper() + word[2:] + word[0].lower() + ('ay') + ' ')
            elif word == sentlist[-1]:
                wordpl = (word[1:] + word[0].lower() + 'ay')
            else:
                wordpl = (word[1:]) + (word[0].lower()) + ('ay') + " "
            psent += wordpl

    print(psent + ' is ' + sent.strip('.') + ' in Pig Latin.')
else:
    print("You didn't input a word or your submission included a number. Please try again.")