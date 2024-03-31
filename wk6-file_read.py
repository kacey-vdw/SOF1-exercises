#read contents of a text file and print it in uppercase

f = open('exo1', 'r') #opens file in read only mode
contents = f.read() #copies text to variable
f.close()

print(contents.upper()) #prints in uppercase
