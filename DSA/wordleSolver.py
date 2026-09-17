
import random; import requests
wordList: list[str]=[]
pastGuesses: list[list[str]]=[]
guessedLetters: list[str]=[]
lastDigit=''

if len(wordList)==0:
    print('Loading word list.')
    wordList=requests.get("https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/73f890e1680f3fa21577fef3d1f06b8d6c6ae318/wordle-La.txt").text.split("\n")
    for element in requests.get("https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/73f890e1680f3fa21577fef3d1f06b8d6c6ae318/wordle-Ta.txt").text.split("\n"):
        wordList.append(element)
    with open('wordle_word_list.csv',"w") as words:
        for word in wordList:
            print(word,file=words)



print('Word list loaded!')
correctWord=['','','','','']
wrongPlace={0:[],1:[],2:[],3:[],4:[]}
wrongLetters={0:[],1:[],2:[],3:[],4:[]}


possibleWords=wordList
currentGuess=random.choice(wordList)
currentGuess='ghost'
guessCount=0
while guessCount<6:
    guessCount+=1
    pastGuesses.append(currentGuess)
    
    score='NA'
    while len(score)!=5:
        score=input(f'{currentGuess}\n')
    if score=='22222':
        guessCount+=6
    else:
        lastDigit=score
        valueDict={}
        for i,digit in enumerate(score):
            digit=int(digit)
            if digit==2:
                correctWord[i]=currentGuess[i]
            elif digit==1:
                wrongPlace[i].append(currentGuess[i])
            else:
                if currentGuess[i] not in wrongLetters[i] and currentGuess[i] not in correctWord:
                    wrongLetters[i].append(currentGuess[i])
            
        for element in wrongLetters:
            if element in correctWord:
                wrongLetters.remove(element)
        for word in wordList:
            wordVal=0
            for i,letter in enumerate(correctWord):
                if letter!='':
                    if letter==word[i]:
                        wordVal+=1
                    elif letter not in word:
                        wordVal=0
                        break
            for i,letter in enumerate(word):
                if letter in wrongLetters[i] or letter in wrongPlace[i]:
                    wordVal=0
                    break
                
                elif letter in wrongPlace[0] or letter in wrongPlace[1] or letter in wrongPlace[2] or letter in wrongPlace[3] or letter in wrongPlace[4]:
                    wordVal+=1
                elif letter in wrongLetters[0] or letter in wrongLetters[1] or letter in wrongLetters[2] or letter in wrongLetters[3] or letter in wrongLetters[4]:
                    wordVal-=1
                if word.count(letter)>1:
                    wordVal-=1
            
            if wordVal in valueDict:
                valueDict[wordVal].append(word)
            else:
                valueDict[wordVal]=[word]
        
        keyList=list(sorted(valueDict.keys(),reverse=True))
        keyList=keyList[0]

        possibleWords = valueDict[keyList]
        print(valueDict[keyList])
        pastGuesses.append(currentGuess)
        removeList=[]
        for element in possibleWords:
            if element in pastGuesses:
                removeList.append(element)
        for element in removeList:
            pastGuesses.remove(element)
        currentGuess = random.choice(possibleWords)
if guessCount==6:
    print('woopsies!')