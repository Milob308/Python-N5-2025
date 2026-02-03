import random

# set up variables needed
counter = 0
mysteryFruits = ["apple", "banana", "bluberry", "kiwi", "mango", "orange", "peach", "pineapple", "rasberry", "strawberry"]
userFruits = []
decision = "Y"

#loop until all of the fruits are valid
while decision == "Y" and counter <6:
    fruits = str(input("please enter your choice of fruits"))
    # validate fruits
    while len(fruits) <4: 
        print("invalid fruit, please select another")
        fruits = str(input("please enter your choice of fruits"))
    # add one to counter
    counter = counter + 1 
    userFruits.append(fruits) # addsuser input to userFruits array
    decision = str(input("please enter Y or N for your decision"))

# generate a mystery fruit and show all other fruits added
num = random.randint(0,9)
for i in range(counter):
    print("the fruits you entered were:", userFruits)
print("the mystery fruit is: ", mysteryFruits[num])

# add 1 to counter for mystery fruit
counter = counter + 1 
# tell the user thr suggested drink
if counter <3 :
    print("I suggest a milkshake")
elif counter == 3 or counter == 4 :
    print("I suggest a smoothie")
else:
    counter >4 
    print("I suggest fruit juice")




