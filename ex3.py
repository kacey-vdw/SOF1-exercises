sentence = str(input("Enter a sentence: ")).lower() #takes lowercase input
shift = int(input("Enter the number of spaces to shift: ")) #takes spaces to shift
cipher = ""
for char in sentence:#every letter in the sentence
    asc = ord(char) #finds ascii value
    if asc > 96 and asc < 123: #if a lowercase letter
        char = str(chr(97 + ((asc-97) + shift)%26)) #performs shift
    cipher += char #adds letter to cipher

print(cipher)

solved = ""
for char in cipher:#every letter in the cipher
    asc = ord(char) #finds ascii value
    if asc > 96 and asc < 123: #if a lowercase letter
        char = str(chr(97 + ((asc-97) - shift)%26)) #performs shift
    solved += char #adds letter to sentence

print(solved)


