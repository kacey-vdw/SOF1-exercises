def merge(listA, listB):
	new_list = []

	if len(listA) == 0: #if listA is empty
		new_list.extend(listB) #add the remaining elements of listB

	elif len(listB) == 0: #if listB is empty
		new_list.extend(listA) #add the remaining elements of listA

	elif listA[0] < listB[0]: #if listA item < listB item
		new_list.append(listA[0]) #add listA item
		new_list.extend(merge(listA[1:len(listA)], listB)) #add merge of listB and remaining listA

	elif listA[0] > listB[0]: #if listA item >listB item
		new_list.append(listB[0]) #add listB item
		new_list.extend(merge(listB[1:len(listB)], listA)) #add merge of listA and remaining listB

	elif listA[0] == listB[0]: #if items are equal
		new_list.append(listA[0]) #add both items
		new_list.append(listB[0])
		new_list.extend(merge(listB[1:len(listB)], listA[1:len(listA)])) #add merge of remaining lists

	return new_list

print(merge([1,3,5,7],[2,4,6,8]))
print(merge([1,2,5,7],[2,4,6,8]))
