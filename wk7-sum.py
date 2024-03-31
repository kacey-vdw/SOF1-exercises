def sum_digits(number):
	#size = len(number) #size of number
	if number >= 0 and number <= 9: #if only 1 digit left
		return number 
	else:
		return (number % 10) + sum_digits(number//10) #return final digit and sum of all prev digits

print(sum_digits(1234)) #10
print(sum_digits(444)) #12
