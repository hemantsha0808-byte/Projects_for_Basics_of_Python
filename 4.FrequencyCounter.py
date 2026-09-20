str = input("Enter the sentence: ")

str = str.lower()

for char in str :
    if(not(char.isalnum() or char == " ")):
        str = str.replace(char, " ")

list = str.split()

NoOfUniqueWords = len(set(list))
keyslist = [None] * NoOfUniqueWords
valueslist = [0] * NoOfUniqueWords

for Word in list:
    j = 0
    while (j < len(keyslist)):
        if (keyslist[j] == Word):
            valueslist[j] += 1
            break
        elif (keyslist[j] == None):
            keyslist[j] = Word
            valueslist[j] += 1
            break
        j += 1


dict = {}
k = 0
while (k<len(keyslist)):
    dict[keyslist[k]] = valueslist[k]
    k += 1

print(dict)