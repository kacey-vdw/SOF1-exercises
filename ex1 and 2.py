def weight_kg(stones,pounds):
	kg = (stones*6.35)+(pounds*0.453)#conversion
	return kg

def distance_km(miles,feet):
	km = (miles*1.609)+(feet*0.3048)#conversion
	return km

def liquid_ltr(gallon,pint):
        litre = (gallon*4.546)+(pint*0.568)
        return ltr

def weight_st(kg):
	stone = kg/6.35
	return stone

def distance_miles(km):
	miles = km/1.609
	return miles

def liquid_gallons(ltr):
	gallon = litre/4.546
	return gallon


######################################

type = 0
while type >3 or type <1:
	type = int(input("1 for weight, 2 for distance, 3 for liquid: "))

if type == 1:
        stones = input("Enter the number of stones: ")
        pounds = input("Enter the number of pounds: ")
        print(stones + " stones and " + pounds + " pounds is " + str(weight_kg(int(stones),int(pounds))) + " kilograms")              

elif type == 2:
        miles = input("Enter the number of miles: ")
        feet = input("Enter the number of feet: ")
        print(miles + " miles and " + feet + " feet is " + str(distance_km(int(miles),int(feet))) + " kilometres")
        
elif type == 3:
        gallons = input("Enter the number of gallons: ")
        pints = input("Enter the number of pints: ")
        print(gallons + " gallons and " + pints + " pints is " + str(liquid_ltr(int(gallons),int(pints))) + " litres")
