dict_1 = {
    "one":1,
    "two":2,
    "five":5
    }
dict_2 = {
    "two":"10",
    "five":"101"
    }
    

def concat_dicoo(dico1, dico2): #function to concatenate two dicts
    dico3 = {} #establish empty dict
    keys1, keys2 = dico1.keys(), dico2.keys() #creates lists of all keys

    for i in keys1:#compare all 1 keys with 2 keys
        for j in keys2:
            if i == j: #if keys are same
                dico1[i] = [i,j] #put corresponding 2 value in list with 1 value
                dico2.pop[j] #remove corresponding 2 pair
                
    
    for key in keys1: #assigns all pairs from dict1 to dict3
        dico3[key] = dico1[key]
    for key in keys2: #assigns all pairs from dict2 to dict3
        dico3[key] = dico2[key]
    print(dico3)



def concat_dico(dico1, dico2):
    dico3 = dico1.copy()
    
    for key in dico2.keys():
        if key in dico3:
            list_values = [dico3[key], dico2[key]]
            dico3[key] = list_values
        else:
            dico3[key] = dico2[key]
    return dico3

print(concat_dico(dict_1, dict_2))
        
