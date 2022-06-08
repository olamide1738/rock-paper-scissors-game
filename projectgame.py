
import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player= None
while player not in choices:
      player = input("Rock Paper or Scissors?").lower()
print("computer :", computer)
print("player: ",player)

if player == computer:
   print("computer :", computer)   
   print("player: ",player)
   print("Tie!")
   
elif player == "rock" :
    if computer == "paper":
         print("computer :", computer)   
         print("player: ",player)
         print("You Lose!")
         
         
elif player == "rock" :
    if computer == "scissors":
         print("computer :", computer)   
         print("player: ",player)
         print("You Win!")
         
elif player == "paper" :
    if computer == "rock":
         print("computer :", computer)   
         print("player: ",player)
         print("You Win!")
         
elif player == "paper" :
    if computer == "scissors":
         print("computer :", computer)   
         print("player: ",player)
         print("You Lose!")
         
elif player == "scissors" :
    if computer == "paper":
         print("computer :", computer)   
         print("player: ",player)
         print("You Win!")
         
elif player == "scissors" :
    if computer == "rock":
         print("computer :", computer)   
         print("player: ",player)
         print("You Lose!")
   
    
