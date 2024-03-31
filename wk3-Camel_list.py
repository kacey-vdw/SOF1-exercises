sentence = str(input("Enter a sentence: ")).lower()
letters = ""
capital_1 = True 

for e in sentence:
    if capital_1 == True:#capitalises current letter
        e = e.upper()
    if (ord(e) > 64 and ord(e) < 91) or (ord(e) > 96 and ord(e) < 123):#adds only letters
        letters += e
        capital_1 = False
    elif e == " ": #if the next letter is the beginning of a word, make it capital
        capital_1 = True

print(letters)

list = [] #empty list for words

current_word = "" #temp string for words for list


for l in range(0,len(letters)): #for every character
    current_word += letters[l] #add letter to word
    if l == len(letters)-1 or(ord(letters[l+1]) > 64 and ord(letters[l+1])) < 91:#if next letter is capital
        list.append(current_word) #^if last letter or next is capital, append
        print(current_word)
        current_word = ""

print(list)
        
