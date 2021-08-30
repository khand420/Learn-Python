
# a = input("What is your Name")
# b = input("How much do you Earn")

# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 so stopping the Program")

# if a.isnumeric():
#     raise Exception("Number are not allowed")

# print(f"Hello{a}")   

c = input("Enter you name: ")
try:
    print(a)
except Exception as e:
    if c == "Khand":
        raise ValueError("Khand is blocked he is not allowed")

    print("Exception Handled (:")        