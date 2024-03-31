# a is power of b if a divisible by b and a/b is a power of b
#recursive function taking a and b, return true if a is power of b, false otherwise

def is_power(a,b):
	if 
	if a%b == 0:
		return False
	else:
		return is_power(a/b, b)

print(is_power(27, 3)) #true
print(is_power(18, 3)) #false
