thisArray = ["kirsty", "amelia", "james", "ali","euan", "joshuaa"]
mostCharacters = len(thisArray[0])
pos = 0 
for index in range(1, len(thisArray)):
    if len(thisArray[index]) >mostCharacters:
        mostCharacters = len(thisArray[index])
        pos = index
print("The name with the most characters is", mostCharacters)