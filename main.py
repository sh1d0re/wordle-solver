import json
words = json.load(open("wordlewords.json"))["words"]
first = [["s", 365], ["c", 198], ["b", 173], ["t", 149], ["p", 141]]
second = [["a", 304], ["o", 279], ["r", 267], ["e", 241], ["i", 201]]
third = [["a", 306], ["i", 266], ["o", 243], ["e", 177], ["u", 165]]
fourth = [["e", 318], ["n", 182], ["s", 171], ["l", 162], ["a", 162]]
fifth = [["e", 422], ["y", 364], ["t", 253], ["r", 212], ["l", 155]]

for one in first:
    for two in second:
        for three in third:
            for four in fourth:
                for five in fifth:
                    word = one[0] + two[0] + three[0] + four[0] + five[0]
                    if word in words:
                        print(word + " : "+ str(one[1] + two[1] + three[1] + four[1] + five[1]))