def to_base10(binary):
    total = 0 #define variable to add values to
    bits = len(binary) #number of bits determines value of each digit
    
    for digit in range(0,bits): #loops for each digit
        if binary[digit] == "1": #if binary digit holds a value
            total += pow(2, bits-1-digit) #adds the digits value

    return total

binary_inp = input("Enter a binary number of any number of bits: ")#takes input

print(to_base10(binary_inp)) #call function
