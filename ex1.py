#save content of string to file called exo1

a_word = "word" #define string
f = open('exo1', 'w') #opens the file for write only, w erases previous contents
f.write(a_word) #writes the string into the file
f.close() #closes file