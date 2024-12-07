#Copy the following in your code editor to replicate the game
import random

# Define ASCII art designs
choices = {
    "rock": """       
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """       
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """       
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

#converts the dictionary's keys into a list (like ["rock", "paper", "scissors"]) and then picks a random item from that list
userchoice=input("Enter your choice: rock,paper or scissors: ")

systemchoice = random.choice(list(choices.keys())) #The line random.choice(list(choices.keys()))
if userchoice in choices:
    print("Computer's choice: ",systemchoice)
    print(choices[systemchoice])

    print("\nYour choice:", userchoice)
    print(choices[userchoice])

if systemchoice=="scissors" and userchoice=="rock":
    print("You won!")
elif systemchoice=="scissors" and userchoice=="paper":
    print("You lost")
elif systemchoice=="rock" and userchoice=="scissors":
    print("You lost!")
elif systemchoice=="rock" and userchoice=="paper":
    print("You won")
elif systemchoice=="paper" and userchoice=="scissors":
    print("You won")
elif systemchoice=="paper" and userchoice=="rock":
    print("You lost")
elif systemchoice==userchoice:
    print("Its a draw")
else:
    print("Invalid choice")


