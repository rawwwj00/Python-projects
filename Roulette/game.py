import time
import os
import random

def welcome():
    for i in range(17):
        x=10
        if i%2==0:
            print("\ Welcome to Roulette |\n")
        else:
            print("| Welcome to Roulette /\n")
        b=35
        c=i
        k=0
        outspace=' '
        inspace=' '
        outspace_count=9
        inspace_count=1
        print((outspace*(outspace_count+2)*2),f'{i-1:02}')
        while b>27:
            print((outspace*outspace_count)*2,f'{b-i:02}',(inspace*(inspace_count+1)*2),f'{c:02}')
            k+=1
            b-=1
            c+=1
            outspace_count-=1
            inspace_count+=2

        while b<29 and b>18:
            print((outspace*outspace_count)*2,f'{b-i:02}',(inspace*(inspace_count+1)*2),f'{c:02}')
            k+=1
            b-=1
            c+=1
            outspace_count+=1
            inspace_count-=2
        print((outspace*(outspace_count+1)*2),f'{18-(i+1):02}')
        if i%2==0:
            print("Loading Game..\n")
        else:
            print("Loading Game.\n")
        time.sleep(0.2)
        
        os.system('cls' if os.name == 'nt' else 'clear')

def rboard(a):
    b=35
    c=1
    k=0
    outspace=' '
    inspace=' '
    outspace_count=9
    inspace_count=1
    if a==0:
        print((outspace*(outspace_count+2)*2),'00','⚪')
    else:
        print((outspace*(outspace_count+2)*2),'00')

    while b>27:
        if a==b:
            print(((outspace*(outspace_count-2))*2),'⚪',b,(inspace*(inspace_count+1)*2),f'{c:02}')
        elif a==c:
            print((outspace*outspace_count)*2,b,(inspace*(inspace_count+1)*2),f'{c:02}','⚪')
        else:
            print((outspace*outspace_count)*2,b,(inspace*(inspace_count+1)*2),f'{c:02}')
        k+=1
        b-=1
        c+=1
        outspace_count-=1
        inspace_count+=2

    while b<29 and b>18:
        if a==b:
            print(((outspace*(outspace_count-2))*2),'⚪',b,(inspace*(inspace_count+1)*2),f'{c:02}')
        elif a==c:
            print(outspace*(outspace_count)*2,b,(inspace*(inspace_count+1)*2),f'{c:02}','⚪')
        else:
            print((outspace*outspace_count)*2,b,(inspace*(inspace_count+1)*2),f'{c:02}')
        k+=1
        b-=1
        c+=1
        outspace_count+=1
        inspace_count-=2
    if a==18:
        print((outspace*(outspace_count+1)*2),'18','⚪')
    else:
        print((outspace*(outspace_count+1)*2),'18')