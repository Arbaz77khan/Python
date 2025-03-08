import random

def abbre(value):
    if value == 1:
        return ("Stone")
    elif value == 2:
        return ("Paper")
    else:
        return ("Scissor")
    
def main(computer,player):
    if (computer == player):
        return("Tie")
    else:
        if (computer == 1):
            if (player == 2):
                return ("Won")
            else:
                return ("Loose")
        elif (computer == 2):
            if (player == 1):
                return ("Won")
            else:
                return ("Loose") 
        else: 
            if (player == 1):
                return ("Won")
            else:
                return ("Loose")
            
print("*****Stone Paper Scissor*****", end="\n")
print("-----You Vs Computer-----", end="\n")
print("Computer played! Now it's your turn", end="\n")

player = int(input("Press 1 : Stone;\tPress 2 : Paper;\tPress 3 : Scissor\nType Here: "))

computer = (random.randint(1, 3))

print("Computer entered : " + abbre(computer) + ";\t" + "You entered : " + abbre(player))

Player_result = main(computer,player)

print("Result : ", Player_result)