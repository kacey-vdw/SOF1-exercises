def rec_sum(numbers):
	size = len(numbers) #length of (sub)list
	if size == 0: #if nothing in list
		return 0 #return 0
	else:
		return numbers[0] + rec_sum(numbers[1:size]) #return 1st item + sum of remaining


print(rec_sum([])) #0
print(rec_sum([1,2,3,4])) #10