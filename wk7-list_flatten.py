def flatten(mlist):
	current_list = []

	for item in mlist: #for each item in the list
		if type(item) is list: #if item is a list
			current_list.extend(flatten(item)) #repeat for the sublist, appending result to currentlist
		else:
			current_list.append(item) #if not a list, append value
	return current_list


print(flatten([1,[2,3],4]))
print(flatten([1,2,3,4]))
print(flatten([1,[2,[3,[4]]]]))
