def training(age, rate):
    m = 208-(0.7*age)
    if rate >= 0.9*m:
        return "interval training"
    elif rate >= 0.7*m:
        return "threshold training"
    elif rate>= 0.5*m:
        return "aerobic training"
    else:
        return "couch potato"

age = int(input("enter age: "))
rate = int(input("enter heart rate: "))
print (str(training(age,rate)))
