



f =  open("khand.txt", "w")
a = f.write("this comming from file handling.py")
print(a)
f.close()

# handle read and write both
f = open("khand.txt", "r+")
print(f.read())
f.write("thank you mere bhai")