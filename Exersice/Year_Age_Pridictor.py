
yearAge = int(input("What is your Age/Year of birth \n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True
else:
    isAge = True


if(yearAge<1900 and isYear):
    print("Yo seem to be the oldest person Alive")
    exit()

if(yearAge>2021):
    print("YOu are not yet born :(")

if isAge:
    yearAge = 2021 - yearAge

print(f"You will be 100 years old in {yearAge + 100}") 

interesteYear = int(input("Enter the year you want to know your age in \n"))
print(f"You will be {interesteYear - yearAge} year old in {interesteYear}")
