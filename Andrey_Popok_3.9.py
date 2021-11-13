word = input("Enter the word: ")
word = word.upper()
for i in range(len(word)):
    if (word[i] in ['A','E','I','O','U']):
        continue
    else:
        print(word[i])
