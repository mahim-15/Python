import random
'''
1 for snake
-1 for water
0 for gun
'''
computer= random.choice([-1,0,1])
youstr =input("Ennter your choice: ")
youDict={ "s":1, "w":-1,"g":0}
reverseDict={1: "Snake",-1: "Water",0:"Gun"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer==you):
    print("It's a draw!")
    
else:
    if(computer-you==-2 or computer-you==1):#-2
      print("You win!")
    elif(computer-you==-1 or computer-you==2):#-1
      print("You Lose!")
    
    else:
      print("something went wrong!")