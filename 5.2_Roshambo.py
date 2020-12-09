'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
wincount=0
losecount=0
done = False
for i in range(1):
    rps = random.randint(1, 3)
rpsuser = input("Rock, Paper, or Scissors? ")
if rps == 1:
    print("Rock!")
elif rps == 2:
    print("Paper!")
else:
    print("Scissors!")
if rpsuser.upper() == "ROCK" and rps == 3:
    print("YOU WIN!!")
    wincount = wincount + 1
elif rpsuser.upper() == "PAPER" and rps == 1:
    print("YOU WIN!!")
    wincount = wincount + 1
elif rpsuser.upper() == "SCISSORS" and rps == 2:
    print("YOU WIN!!")
    wincount = wincount + 1
elif rpsuser.upper() == "ROCK" and rps == 1:
    print("TIE!!")
elif rpsuser.upper() == "PAPER" and rps == 2:
    print("TIE!!")
elif rpsuser.upper() == "SCISSORS" and rps == 3:
    print("TIE!!")
else:
    print("YOU LOSE!!")
    losecount = losecount + 1
while not done:
    quit = input("Do you want to quit? ")
    if quit.upper() == "YES" or quit.upper() == "Y":
        done = True
    else:
        for i in range(1):
            rps = random.randint(1, 3)
        rpsuser=input("Rock, Paper, or Scissors? ")
        if rps==1:
            print("Rock!")
        elif rps==2:
            print("Paper!")
        else:
            print("Scissors!")
        if rpsuser.upper()=="ROCK" and rps==3:
            print("YOU WIN!!")
            wincount=wincount+1
        elif rpsuser.upper()=="PAPER" and rps==1:
            print("YOU WIN!!")
            wincount = wincount + 1
        elif rpsuser.upper()=="SCISSORS" and rps==2:
            print("YOU WIN!!")
            wincount = wincount + 1
        elif rpsuser.upper() == "ROCK" and rps == 1:
            print("TIE!!")
        elif rpsuser.upper() == "PAPER" and rps == 2:
            print("TIE!!")
        elif rpsuser.upper() == "SCISSORS" and rps == 3:
            print("TIE!!")
        else:
            print("YOU LOSE!!")
            losecount = losecount+1
print("Your Win Count: ",wincount)
print("Your Lose Count",losecount)
if wincount>losecount:
    print("You've Won Overall")
elif losecount>wincount:
    print("You've Lost Overall")
else:
    print("You've Tied Overall")