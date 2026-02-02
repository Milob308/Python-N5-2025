home = 0
away = 0
period = 1
while period <= 3:
    print("------")
    print("Home-",home,"-",away,"- Away")
    print("period",period)
    print("------")
    print("")
    option= input("Enter (h)ome, (a)way or (x) to end period: ")
    while option != "h" and option != "a" and option != "x":
        print("Incorrect option. Try again.")
        option = input("Enter (h)ome, (a)way or (x) to end period: ")
    if option == "h":
        home = home + 1
    if option == "a": 
        away = away + 1     
    if option == "x":
       period = period + 1