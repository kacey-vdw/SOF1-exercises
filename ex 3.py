def map_list(keys,values):
    
    if len(keys) != len(keys):
        return "none"
    
    elif len(keys) != len(set(keys)): #if set and list are same length, there are duplicate items
        print("There are duplicate items in the keys list")
        return "none"
    
    else:
        dico = {}
        for x in range(0, len(keys)):
            dico[keys[x]] = values[x]
        return dico

key_list = ["Name", "Colour", "Age"]
value_list = ["John", "Blue", "30"]
dico = map_list(key_list, value_list)

def reverse_dico(dico):
    
    if len(dico.values()) != len(set(dico.values())):
        print("There are duplicate values")
        return "none"
    else:
        dico_new = {}
        values = dico.values()
        keys = dico.keys()
        for key in dico.keys():
            dico_new[dico[key]] = key
            
        dico = dico_new.copy()
        return dico

print(reverse_dico(dico))
