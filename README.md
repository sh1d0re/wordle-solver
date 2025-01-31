# Solving Wordle (Literaly)

## Discovering the strategy
### Whats the most convinient first attempt you can make in wordle?
> What is the most used letter in wordle? Here is a dictionary of how many letters exist in the wordle word database:
>
> ```{'a': 975, 'b': 280, 'c': 475, 'd': 393, 'e': 1230, 'f': 229, 'g': 310, 'h': 387, 'i': 670, 'j': 27, 'k': 210, 'l': 716, 'm': 316, 'n': 573, 'o': 753, 'p': 365, 'q': 29, 'r': 897, 's': 668, 't': 729, 'u': 466, 'v': 152, 'w': 194, 'x': 37, 'y': 424, 'z': 40}```
>
> As expected, vowels are frequently used letters in the wordle database, since vowels are the most used letter to construct a word. Notably, letters such as "e" appeared 1230 times in the database.

> I also found out what are the letters that appear in indivisual digit (1~5):
>
> Letter 1: ```{'s': 365, 'c': 198, 'b': 173, 't': 149, 'p': 141, 'a': 140, 'f': 135, 'g': 115, 'd': 111, 'm': 107, 'r': 105, 'l': 87, 'w': 82, 'e': 72, 'h': 69, 'v': 43, 'o': 41, 'n': 37, 'i': 34, 'u': 33, 'q': 23, 'j': 20, 'k': 20, 'y': 6, 'z': 3}```
>
> Letter 2: ```{'a': 304, 'o': 279, 'r': 267, 'e': 241, 'i': 201, 'l': 200, 'u': 185, 'h': 144, 'n': 87, 't': 77, 'p': 61, 'w': 44, 'c': 40, 'm': 38, 'y': 22, 'd': 20, 'b': 16, 's': 16, 'v': 15, 'x': 14, 'g': 11, 'k': 10, 'f': 8, 'q': 5, 'z': 2, 'j': 2}```
>
> Letter 3: ```{'a': 306, 'i': 266, 'o': 243, 'e': 177, 'u': 165, 'r': 163, 'n': 137, 'l': 112, 't': 111, 's': 80, 'd': 75, 'g': 67, 'm': 61, 'p': 57, 'b': 56, 'c': 56, 'v': 49, 'y': 29, 'w': 26, 'f': 25, 'k': 12, 'x': 12, 'z': 11, 'h': 9, 'j': 3, 'q': 1}```
>
> Letter 4: ```{'e': 318, 'n': 182, 's': 171, 'l': 162, 'a': 162, 'i': 158, 'c': 150, 'r': 150, 't': 139, 'o': 132, 'u': 82, 'g': 76, 'd': 69, 'm': 68, 'k': 55, 'p': 50, 'v': 45, 'f': 35, 'h': 28, 'w': 25, 'b': 24, 'z': 20, 'x': 3, 'y': 3, 'j': 2}```
>
> Letter 5: ```{'e': 422, 'y': 364, 't': 253, 'r': 212, 'l': 155, 'h': 137, 'n': 130, 'd': 118, 'k': 113, 'a': 63, 'o': 58, 'p': 56, 'm': 42, 'g': 41, 's': 36, 'c': 31, 'f': 26, 'w': 17, 'i': 11, 'b': 11, 'x': 8, 'z': 4, 'u': 1}```

> To find out the best first attempt in wordle, I decided to adopt the **point system**, where if a word contains the most points than the others. 
> 
> | Letter 1  | Letter 2  | Letter 3  | Letter 4  | Letter 5  | Word  | Points |
> | --------- | --------- | --------- | --------- | --------- | ----- | ------ |
> | `s [365]` | `a [304]` | `a [306]` | `e [318]` | `e [422]` |       |        |
> | `c [198]` | `o [279]` | `i [266]` | `n [182]` | `y [364]` |       |        |
> | `b [173]` | `r [267]` | `o [243]` | `s [171]` | `t [253]` |       |        |
> | `t [149]` | `e [241]` | `e [177]` | `l [162]` | `r [212]` |       |        |
> | `p [141]` | `i [201]` | `u [165]` | `a [162]` | `l [155]` |       |        |
> |           |           |           |           |           |       |        |
> | `s [365]` | `a [304]` | `i [266]` | `n [182]` | `t [253]` | **SAINT** |        |
> | `s [365]` | `a [304]` | `i [266]` | `n [182]` | `t [253]` | **SAINT** |        |
