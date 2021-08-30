

def funargs(normal, *argskhan, **kwargsRaza):
    
    # 1.for Normal Arguments 
    print(normal)

    # 2.for *args Arguments 
    for item in argskhan:
        print(item)

    #3. for **kwargs Arguments 
    print("\n Now I would Like to introduce some of Arguments")
    for key, value in kwargsRaza.items():
        print(f"{key} is a {value}")


khan = ["Danish", "Adil", "Moti", "Raza", "Sarkar"]

normal = ["I am Normal Argument and the students are:"]

kw = {"Moti":"Dog", "khand":"Actor", "Akram":"Nashedi"}

funargs(normal, *khan, **kw)


