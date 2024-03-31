#function to calculate sum of all ints in file

def sum_from_file(filename):
	f = open(filename, 'r') #opens file in read mode
	numbers_list = f.readlines() #copies each line to a list
	f.close() #closes file

	total = 0
	current_num = ""
	new_list = []

	for line in numbers_list:
		new_list += line[0:len(line)].split(" ") #appends onto new list a line from numbers list with only the numbers

	for item in new_list: #iterates through each item in new list
		if not item.isnumeric(): #it item is not numeric ie. has \n at the end
			item = item[0:len(item)-1] #removes \n
		total += int(item) #adds int of item to total
	print(total)

sum_from_file('numbers.txt')