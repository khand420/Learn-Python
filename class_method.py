class Employee:
    no_of_leaves = 43

    def __init__ (self, aname, asalary, arole):
        self.aname = name
        self.asalary = salary
        self.arole = role

    def printDetails(self):
        return f"The name is {self.name} salary.is {self.salary} and role is {self.role}"

    @classmethod   
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


khand = Employee("khand", 234, "cloud engineer")
raza = Employee("muskan", 222, "bio-tech-Engineer")

raza.change_leaves(43)

print(khand.change_leaves)
