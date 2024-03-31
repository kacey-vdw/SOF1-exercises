#function takes filename and sentences as parameters, writes list contents onto different lines in file
sentences_list = ["What are you", "doing tomorrow", "evening? I have", "to take out the", "bins."]

def save_list2file(sentences, filename): #takes sentences and file name as parameters
		f = open(filename, 'w') #opens file in write mode
		for item in sentences: #iterates over each item in the list
			f.write(item+'\n') #writes current item into a new line in the file
		f.close() #closes the file

save_list2file(sentences_list, 'exo1')
