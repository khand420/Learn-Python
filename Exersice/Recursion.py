


# FACTORIAL .....

# n! = n* n-1 * n-2 * n-3... 1.
# n! = n * (n-1)
# def factorial(n):
#     """
#     param n: integer
#     return: n* n-1 * n-2 * n-3 ...... 1.
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac* (i+1)
#     return fac

# def factorial_recursion(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursion(n-1)

    

# number = int(input("Enter the Number: "))
# print("Factorial Using Iterative method", factorial_recursion(number))
# print(factorial(number))



# FIBONACCI NUMBER

def fibonacci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print(fibonacci(number))