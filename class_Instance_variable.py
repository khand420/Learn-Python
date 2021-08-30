class Employee:
    no_of_leaves = 8
    pass


khand = Employee()
raza = Employee()

khand.name = "DANISH"
khand.salary = 455
khand.role = "cloud Engineer"

raza.name = "muskan"
raza.salary = 3349
raza.role = "bio-tech engineer"

# dict are built in attributes in class in python
print(raza.__dict__)

raza.no_of_leaves= 343
khand.no_of_leaves = 90
print(Employee.no_of_leaves)


print(khand.__dict__)

