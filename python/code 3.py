leapyear = input("Is it a leap year? (y/n): ")
weekday = input("Enter the week day for January 1st (MO/TU/WE/TH/FR/SA/SU): ")
if weekday == "SA":
    noSaturdays = 53
elif weekday == "FR" and leapyear == "y":
    noSaturdays = 53
else:
    noSaturdays = 52
print("There are",noSaturdays,"Saturdays this year.")


