rows = int(input("Enter the number of rows for the triangle: "))

rows_list = []
current_row = ""

for row in range(0, rows):
    counter = row + 1
    while counter > 0:
        if counter % 2 == 0:
            current_row += "0"
        else:
            current_row += "1"
        counter -= 1
    rows_list.append(current_row)
    current_row = ""

for item in rows_list:
    print(item)
