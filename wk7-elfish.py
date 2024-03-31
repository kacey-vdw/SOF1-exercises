def iselfish(compare, word):

	if compare == "": #if all letters have been found
			return True
	elif len(word) != 0: #if not all letters in word have been checked
		if word[0] in compare: #if current letter is a letter to be found
			return iselfish(compare.replace(word[0],""),word[1:]) #recursion remove found letter from letters to be found and word
		elif len(word) == 1: #if this is the last letter
			return False
		else: #if letter not found but still letters to be checked
			return iselfish(compare, word[1:])
	else:
		return False


		

print(iselfish("elf","tasteful")) #true
print(iselfish("elf","whiteleaf")) #true
print(iselfish("elf","mango")) #false
print(iselfish("kc","kacey")) #true
print(iselfish("gay","egregiously")) #false
