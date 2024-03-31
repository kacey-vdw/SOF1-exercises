months = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

print(months)

numerals = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}

print(numerals)

elements = {
    "H":"Hydrogen",
    "Li":"Lithium",
    "Na":"Sodium",
    "K":"Potassium",
    "Rb":"Rubidium",
    "Cs":"Caesium",
    "Fr":"Francium"
}

print(elements)

roman = {}
roman[100000]="T"
roman[1000]="M"
roman[500]="D"
roman[100]="K"
roman[50]="L"
roman[10]="X"
roman[5]="V"
roman[1]="I"

roman[100] = "C"
roman.pop(100000)

print(roman)

def display_dico(dico): #function to display all key value pairs in a dict
    keys = dico.keys() #makes a list of all keys
    for key in keys: #loops for all keys
        print(str(key) + " --> " + str(dico[key])) #prints key and value

display_dico(elements)

