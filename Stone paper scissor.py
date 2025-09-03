import random as rd

name = input("What is your name? = ")
print(f"\nHELLO {name}, Welcome to \"stone paper scissor game\" like squid game")
print(input())
print('''\nyou are good guy, So choose first..
stone for 1
papar for 2
scissor for 3
   ''')
print(input())
ch = int(input("\nchoose the numner between 1, 2, 3 ="))
a = ["stone", "paper", "scissor"]
if ch == 1 :
    print(f"ohh, amazing \"{a[0]}\"")
elif ch == 2:
    print(f"ohh, amazing \"{a[1]}\"")
elif ch == 3:
    print(f"ohh, amazing \"{a[2]}\"")
else:
    print("\nhey, only 1, 2, 3. do not forget")
    exit()
print(input())
# choises = ["stone", "paper", "scissor"]
print(f"\ngood choise sweetheart, now my turn..")
print(input())
choises = ["stone", "paper", "scissor"]
computer_ch = rd.choice(choises)
print("mera he ye =",computer_ch)
if computer_ch == a[ch-1]:
    print("ohhh, same pinch")
elif (computer_ch == "stone" and a[ch-1] == "paper") \
           or (computer_ch == "scissor" and a[ch-1] == "stone") \
            or (computer_ch == "paper" and a[ch-1] == "scissor"):
    print(f"hey {name}, you win... but next time i will beat you ")
else:
    print(f"hey {name}, i win... better luck next time")