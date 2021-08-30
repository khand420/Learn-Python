

print("Enter the numbers of the list one by one \n")
size = int(input("Enter size of List \n"))

# Initialize a blank list
myList = []

# Take the User input one by one
for i in range(size):
    myList.append(int(input("Enter list Element \n")))

print(f"Your list is {myList}")    

reverse1 = myList[:]
reverse1.reverse()
print(f"First Reverse Technique List = {myList} Reverse = {reverse1}")
print(f"Second Reverse Technique List {myList} Reverse =  {myList[::-1]}")


reverse2 = myList[:]
for i in range(len(reverse2)//2):
    reverse2[i], reverse2[len(reverse2) -i -1] = reverse2=[(len(reverse2) -i -1], 