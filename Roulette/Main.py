from game import *
import time
import os

while True:
    welcome()
    c=int(input("Enter number of players: "))

    players_point={}
    players_bet={}
    x=[]
    for i in range(c):
        c=input(f"Enter name of player {i+1}: ")
        number=int(input("Enter your number: "))
        if number in x:
            print("Two players can't have same number")
            os._exit(0)
        elif number>36:
            print("You cannot take number greater than 36 !!")
            os._exit(0)
        else:
            x.append(number)
            players_point[c]=number
        bet=int(input(f"Player {i+1}'s bet: $"))
        players_bet[c]=bet
        os.system('cls' if os.name == 'nt' else 'clear')

    a=list(players_point.values())
    d=list(players_point.keys())
    f=list(players_bet.values())
    b=random.randint(0,36)


    time.sleep(1)
    for z in range(len(a)):
        print(f"{d[z]} has chosen {a[z]} with a bet of ${f[z]}")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    rboard(b)

    if b in a:
        e=d[a.index(b)]
        print(f"\n{e} won the game and won ${sum(f)}")
    else:
        print(f"\nNo one won the game !! Winning number: {b}")
    z=input("Want to play again? (Y/N): ")
    p=z.lower()
    if p=='y':
        print("Restarting the game")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    else:
        print("Thank you for playing!! Hope you come again :)")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        break