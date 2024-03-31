def sum_lists(list_2D):
    output = []
    total = 0

    for row in data:
        for value in row:
            total += value #adds all values to total
        output.append(total)#adds final total to list
        total = 0 #resets total back to 0
    return(output)
    
data = [[1,2,3],[2],[1,2,3,4]]
print(sum_lists(data))
