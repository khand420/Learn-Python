

num = int(input("Enter the Number You want to Factor !\n"))
mn= int(input("Enter the minimum number to check..\n"))
mx = int(input("Enter the maximum number to check..\n"))


for i in range(mn, mx+1):
    if num%i ==0:
        print(f"{i} is a divisor fo {num}")