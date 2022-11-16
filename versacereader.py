lyrics = []
let = 4
file1 = open("../../AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/migosversace.txt", "r")
migos = file1.read()

##print(migos)

offset = migos.split()
print(offset)

word = 'Versace'
word2 ='Versace,'
word3 = '"Versace"'
j = 0
k = 0
lyrics_length = len(lyrics)
print(lyrics_length)

for i in offset:
    if i == word:
        j += 1
    elif i == word2:
        j += 1
    elif i == word3:
        j += 1

for i in offset:
    k += 1

print("In the song Versace by the Migos the word Versace is used {} time".format(j))

ratio = j/k * 100
print("That mean {} percent of the song is the word versace".format(ratio))



file1.close()
####