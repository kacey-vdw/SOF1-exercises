def sum_digits(number):
    digits = []
    for char in number:
        digits.append(int(char))
    total = 0
    for num in range(0, len(digits)):
        total += digits[num]
    return total

num_input = input("Enter a number to find the sum of the digits: ")

print("The sum of the digits of " + str(num_input) + " = " + str(sum_digits(num_input)))
    
        
