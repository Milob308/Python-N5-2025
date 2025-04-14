averagetemperature = []
temperature= []
for index in range (7):
    temp = int(input("Enter the temperature"))
    while temp < -20 or temp >50:
        print("this is not a valid temperature")
        temp = int(input("Enter the temperature"))
    temperature.append(temp)

        




