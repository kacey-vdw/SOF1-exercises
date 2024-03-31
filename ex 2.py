def pairwise_digits(num_a, num_b):
    num_a = str(num_a)
    num_b = str(num_b)
    binary = ""
    length = min(len(num_a), len(num_b)) #shortest length
    addon = max(len(num_a), len(num_b)) - length #difference between min and max

    for digit in range(0, length): #only compares for the length of the shortest num
        if num_a[digit] == num_b[digit]:
            binary += "1"
        else:
            binary += "0"

    binary += "0"*addon #adds 0s on the end where there are no digits to compare

    return binary

#number_a = input("Enter a number: ")
#number_b = input("Enter another number: ")

print(pairwise_digits(1213, 2113))
print(pairwise_digits(1213, 10435))
