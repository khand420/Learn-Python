
class Employee:
    no_of_leaves = 0
    var = 34
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The Name is {self.name}. and the Salary is {self.salary} and role is {self.role}"    


class Player:
    var = 9
    no_of_games = 4
    def __init__(self, bname, bgame):
        self.name = bname
        self.game = bgame

    def printDetails(self):
        return f"The name is {self.name} and game is {self.game}"


class CoolProgrammer(Player, Employee):
    var = 455
    language = "C++"
    def printLanguage(self):
        print(self.language)

obj = Employee("khand", 244, "Instructor")
obj2 = Employee("Rohit", 344, "Student")

obj3 = Player("Asif", ["Cricket"])
obj4 = Player("Aman", ["Football"])

det = obj4.printDetails()
obj4.printDetails()
print(det)
print(obj4.var)