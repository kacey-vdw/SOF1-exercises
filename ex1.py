#recursive function to check palindrome, return true/false
def ispalindrome(word):
	word = word.lower()
	left_pointer = 0
	right_pointer = len(word)-1

	if len(word) == 1: #only 1 character
		return True

	if punct(word[left_pointer]): #if left char is punctuation
		left_pointer += 1                #next character
	if punct(word[right_pointer]):#if right char is punctuation
		right_pointer -= 1               #next character

	if word[left_pointer] == word[right_pointer]: #first and last characters are same
		return ispalindrome(word[left_pointer+1:right_pointer]) #calls itself using substring between first and last char
	else:
		return False #not a palindrome

def punct(character):
	if (ord(character) >= 33 and ord(character) <= 47) or (ord(character) >= 58 and ord(character) <= 64): #if char within punctuation ascii ranges
		return True #is punctuation
	else:
		return False
