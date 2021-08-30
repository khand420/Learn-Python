

f1 = open("khand.txt")

try: 
    f = open("does.text")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")    

finally:
     print("Run this anyway....") 
    #  f.close()
     f1.close()   