import os
import json

wordsDB = json.load(open("wordlewords.json"))["words"]
possibleWords = {}
for alphabet in list("abcdefghijklmnopqrstuvwxyz"):
    possibleWords[alphabet] = "\x1b[40m"

def splitLines():
    print("".join(["─" for i in range(os.get_terminal_size().columns)]))

def removeInvalidWords(invalidLetters: list, includedWords: str, matchedWords: str):
    unmatchingWords = []
    for word in wordsDB:
        remove = False
        for i in range(5):
            if len(invalidLetters) > i:
                if invalidLetters[i] in word:
                    remove = True
            if len(includedWords) > i:
                if not (includedWords[i] == "-"):
                    if (word[i] == includedWords[i]):
                        remove = True
                    if (not includedWords[i] in word):
                        remove = True
            if len(matchedWords) > i:
                if (not matchedWords[i] == "-") and (not word[i] == matchedWords[i]):
                    remove = True
            if remove:
                unmatchingWords.append(word)
                break
    return(unmatchingWords)

def checkIfValidResult(result: str):
    resultSet = set(list(result))
    for validInput in list("123"):
        if validInput in resultSet:
            resultSet.remove(validInput)
    validity = False
    if len(resultSet) == 0:
        validity = True
    return(validity)

def checkIfValidAttempt(attemptedInput: str):
    wordsDBInstance = json.load(open("wordlewords.json"))["words"]
    return(
        (len(attemptedInput) == 5) and (attemptedInput in wordsDBInstance)
        )
    
def getWordFrequency():
    first, second, third, fourth, fifth = [], [], [], [], []
    for word in wordsDB:
        first.append(word[0])
        second.append(word[1])
        third.append(word[2])
        fourth.append(word[3])
        fifth.append(word[4])
    firstFrequency, secondFrequency, thirdFrequency, fourthFrequency, fifthFrequency = [], [], [], [], []
    for alphabet in possibleWords.keys():
        firstFrequency.append([first.count(alphabet), alphabet])
        secondFrequency.append([second.count(alphabet), alphabet])
        thirdFrequency.append([third.count(alphabet), alphabet])
        fourthFrequency.append([fourth.count(alphabet), alphabet])
        fifthFrequency.append([fifth.count(alphabet), alphabet])
    return({
        "first": list(reversed(sorted(firstFrequency))),
        "second": list(reversed(sorted(secondFrequency))),
        "third": list(reversed(sorted(thirdFrequency))),
        "fourth": list(reversed(sorted(fourthFrequency))),
        "fifth": list(reversed(sorted(fifthFrequency)))
    })

def findBestAttempt(searchLimit: int):
    wordFrequency = getWordFrequency()
    first = wordFrequency["first"][:int(searchLimit)]
    second = wordFrequency["second"][:int(searchLimit)]
    third = wordFrequency["third"][:int(searchLimit)]
    fourth = wordFrequency["fourth"][:int(searchLimit)]
    fifth = wordFrequency["fifth"][:int(searchLimit)]
    rankings = {}
    for one in first:
        for two in second:
            for three in third:
                for four in fourth:
                    for five in fifth:
                        word = one[1] + two[1] + three[1] + four[1] + five[1]
                        if word in wordsDB:
                            rankings[int(one[0] + two[0] + three[0] + four[0] + five[0])] = word
    rankingKey = list(reversed(sorted(rankings)))[:5]
    return([rankings[i] for i in rankingKey])

def filterAndCompareResultAndInput(attemptedInput: str, inputResult: str):
    includedWords = ""
    invalidWords = ""
    matchedWords = ""
    for i in range(len(inputResult)):
        if inputResult[i] == "1":
            invalidWords += attemptedInput[i]
            possibleWords[attemptedInput[i]] = "\x1b[30;40m"

        if inputResult[i] == "2": 
            includedWords += attemptedInput[i]
        else: includedWords += "-"

        if inputResult[i] == "3":
            matchedWords += attemptedInput[i]
        else: matchedWords += "-"
    return({
        "invalidWords": invalidWords,
        "includedWords": includedWords,
        "matchedWords": matchedWords
    })

os.system("clear")

wordOutput = ""
for alphabet in possibleWords.keys():
    wordOutput += f"{possibleWords[alphabet] + alphabet}\x1b[0m"
wordOutput += "\x1b[0m"

columnSize = os.get_terminal_size().columns
print("╷ ╷ ┌─┐ ┌┐  ┌─╮ ╷   ┌─╴     ┌─╴ ┌─┐ ╷   ╷ ╷ ┌─╴ ┌┐  ".center(columnSize))
print("│││ │ │ ├┴┐ │ │ │   ├─╴     └─┐ │ │ │   │┌┘ ├─╴ ├┴┐ ".center(columnSize))
print("└┴┘ └─┘ ╵ ╵ └─╯ └─╴ └─╴     ╶─┘ └─┘ └─╴ └┘  └─╴ ╵ ╵ ".center(columnSize))
print("\x1b[3mCreator: Sh1d0re / License: GPL-3.0 / Language: Python".center(columnSize))
splitLines()
print(wordOutput + "Enter \x1b[100m1: BLACK\x1b[0m, \x1b[43m2: YELLOW\x1b[0m, \x1b[42m3: GREEN\x1b[0m".rjust(os.get_terminal_size().columns+2))
splitLines()
print(" - Top 5 Efficient First Attempts - ".center(os.get_terminal_size().columns))
print(f"\x1b[3mslate - [ 1432 ] / sauce - [ 1406 ] / slice - [ 1403 ] / shale - [ 1399 ] / saute - [ 1395 ]\x1b[0m")
for trial in range(6):
    while True:
        attemptedInput = input("Input attempted input: ").lower()
        if checkIfValidAttempt(attemptedInput):
            break
        else:
            print("\x1b[31;3m[!] Input was not valid! Only inputs thats are len > 5 and a word is acceptable\x1b[0m")

    while True:
        result = input("Input result of input: ").lower()
        if checkIfValidResult(result):
            break
        else:
            print("\x1b[31;3m[!] Input was not valid! Only inputs of 1 or 2 or 3 is acceptable\x1b[0m")

    os.system("clear")

    convertedInput = filterAndCompareResultAndInput(attemptedInput, result)
    for i in removeInvalidWords(
            list(convertedInput["invalidWords"]),
            convertedInput["includedWords"],
            convertedInput["matchedWords"]):
        wordsDB.remove(i)

    wordOutput = ""
    for alphabet in possibleWords.keys():
        wordOutput += f"{possibleWords[alphabet] + alphabet}\x1b[0m"
    wordOutput += "\x1b[0m"

    print(wordOutput + "Enter \x1b[100m1: BLACK\x1b[0m, \x1b[43m2: YELLOW\x1b[0m, \x1b[42m3: GREEN\x1b[0m".rjust(os.get_terminal_size().columns+2))
    splitLines()
    print(" - All Candidates - ".center(os.get_terminal_size().columns))
    print(str(wordsDB).replace("'", ""))
    splitLines()
    print(" - Top 10 Efficient Attempts - ".center(os.get_terminal_size().columns))
    print(str(findBestAttempt(10)).replace("'", ""))