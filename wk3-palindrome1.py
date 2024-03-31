numbers = str(input("Enter a series of numbers, separated by spaces: "))
numbers += "x"

list_nums = []
current_num = ""

for element in range(0,len(numbers)):
    if numbers[element] != " " and numbers[element] != "x":
        current_num += numbers[element]
        
    else:
        list_nums.append(int(current_num))
        current_num = ""
print(list_nums)

even_nums = 0

for num in range(0, len(list_nums)):
    if list_nums[num] % 2 == 0:
        even_nums += 1

print("The input contains " + str(even_nums) + " even numbers.")
    
    
