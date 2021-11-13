word = input("Enter the word: ")
word = word.upper()
new_word = ''
for i in range(len(word)):
    if (word[i] in ['A','E','I','O','U']):
        continue
    else:
        new_word += word[i]
print(new_word)