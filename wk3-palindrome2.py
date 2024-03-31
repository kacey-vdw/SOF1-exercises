word = str(input("Enter a word/sentence to check if it is a palindrome: ")).lower()
reverse = ""
new_word = ""

for e in word: #iterates through word, only selecting letters and copy to new word
    if (ord(e) > 64 and ord(e) < 91) or (ord(e) > 96 and ord(e) < 123):
        new_word += e

for element in reversed(new_word): #iterates through backwards
    reverse += element

if reverse == new_word: #if reverse is equal, is palindrome
    print("Is a palindrome")
else:
    print("Is not a palindrome")
