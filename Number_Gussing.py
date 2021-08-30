

n = 10
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")

while(number_of_guesses <=9):
    guess_number = int(input("Guess the Number :\n"))
    
    if guess_number<10:
        print("You enter less number please input greater number! \n")
    elif guess_number>10:
        print("You enter greater number please input smaller number! \n")
    else:
        print("You Won\n")
        print(number_of_guesses, "NO. of guesess be took to finish.")

    print(9-number_of_guesses,"NO. of guesses left!")
    number_of_guesses - number_of_guesses + 1

if(number_of_guesses > 9):
    print("Game Over :(")                