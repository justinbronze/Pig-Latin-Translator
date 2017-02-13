print('Welcome to the Pig Latin Translator. Input your word below.')
word = (input("Word to be translated: "))
if len(word) > 0 and word.isalpha():
    wordpl = (word[1:]) + (word[0].lower()) + ('ay')
    wordpl = (wordpl[0].upper() + wordpl[1:])
    print(wordpl + ' is ' + word + ' in Pig Latin.')
else:
    print("You didn't input a word. Please try again.")