import random

chance=5
user_score=0
computer_score=0
lis=['s','r','p']



def play():
    global chance,user_score,computer_score
    computer_choice=random.choice(lis)
    user_choice=input(("Choose--> \nS for scissors\nP for paper\nR for rock:\n")).lower()
    if computer_choice==user_choice:
        print(f"{computer_choice} and {user_choice}\n Its a tiee!!")
        user_score+=0
        computer_score+=0
        print(f"Opponent score:{computer_score}\nYour score:{user_score}\nChances left : {chance}")
    elif user_choice=="r" and computer_choice=="p":
        computer_score+=1
        chance-=1
        print(f"{computer_choice} and {user_choice}\nOh no, Your opponent gets one point\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    elif user_choice=="r"and computer_choice=="s":
        user_score+=1
        chance-=1
        print(f"{computer_choice} and {user_choice}\nYou won this round!\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    elif user_choice=="p"and computer_choice=="r":
        user_score+=1
        chance-=1
        print(f"{computer_choice} and {user_choice}\nYou won this round!\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    elif user_choice=="p" and computer_choice=="s":
        chance-=1
        computer_score+=1
        print(f"{computer_choice} and {user_choice}\nOh no, Your opponent gets one point\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    elif user_choice=="s" and computer_choice=="r":
        chance-=1
        computer_score+=1
        print(f"{computer_choice} and {user_choice}\nOh no, Your opponent gets one point\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    elif user_choice=="s"and computer_choice=="p":
        chance-=1
        user_score+=1
        print(f"{computer_choice} and {user_choice}\nYou won this round!\nOpponent score:{computer_score}\n \
Your score:{user_score}\nYou have {chance} chances left")
    else:
        print("Sorry, Invalid input.")

while chance>0:
    play()

if chance==0:
        print(f"\n\n******************** FINAL RESULTS **********************\
\n*  YOUR score is {user_score}\n*  OPPONENTS score is {computer_score}")
        if user_score>computer_score:
            print("*  You have WON !!")
        else:
            print("*  You have LOST")
        print("*********************************************************")







    