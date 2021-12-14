# Inporting random.
import random

# number of chances to be given to the user to guess the number
# or it is the inputs given by user into input box here number of chances are 5
chance = 0

# Generating a random number between 1 to 9. 
num = random.randint(1,9)

# Getting how many correct answers you got
correct = 0

print("""Instructions
Enter any one random number between 1 to 9.
If your number matches the number given by the system you get one point.
If not then your one chance will be deducted
You only have 5 chances Good Luck!
""")

# While loop to count the number of chances
while chance < 5:
 
 # Enter a number between 1 to 9
 guess = int(input("Try Your luck: "))
 
 # Compare the user entered number with the number to be guessed
 if num == guess:
 # if number entered by user is same as the generated
    print("Your guess was correct you won!!")
 # Increase the value of correct answer by 1
    correct += 1
# To increase the chnce if the number is correct
    chance -= 1
  
 # Check if the user entered number is smaller than the generated number
 elif guess < num:
    print("Your guess was too low try one more time")
    print("The number is: ",num)
    
 # The user entered number is greater than the generated number
 else:
    print("Your guess was too high try one more time")
    print("The number is: ",num)
    
  # Increase the value of chance by 1
 chance += 1
 
# Check whether the user guessed the correct number
if not chance < 5: 
   print("You lose!! The number is ",num)
   print("You got ",correct," answer(s) correct.")
