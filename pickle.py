import pickle

# pickling the python object 

# cars = ["Audi", "BMW", "MARUTI SUZUKI", "YAMAHAN", "HERO-HONDA"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close


file ="mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))