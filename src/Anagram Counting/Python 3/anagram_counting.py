import sys


# number from 0 - 100 with their factorial values
dict_factorials = {0: 1}

for i in range(1, 101):
    dict_factorials[i] = i * dict_factorials[i - 1]


for line in sys.stdin:
    word = str(line.split()[0])  # checks first word in input
    occurrence = {} # How many times a char is repeated

    for character in word:
        if ord(character) in occurrence:
            occurrence[ord(character)] += 1 
        else:
            occurrence[ord(character)] = 1


    value = dict_factorials[len(word)]

    for key in occurrence:
        value = value // dict_factorials[occurrence[key]]

    print(value)
