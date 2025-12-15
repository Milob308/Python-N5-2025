import random

endings = ["ing","end","axe","gex","goh"]
NumStudents = int(input("please enter the number of students: "))
for index in range(NumStudents):
    name = input("please enter the first three letters of the student's names: ")
    while len(name) !=3:
        name = input("please enter the first three letters of the student's names: ")
        print ("invalid name")
    number = random.randint(0,4) 
    username = (name + endings[number])
    print("your username is,",username)
    