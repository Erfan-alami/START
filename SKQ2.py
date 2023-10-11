
#S=sang,K=kaghaz,Q=qeichi
import random

i=0#variables
winc=0 
winu=0

for i in range(1,100):# for loop for cycling the game
 if winu==4 :
        print("*********USER WIN*********")
        break#statement for User or system wining
 elif winc==4:
      print("*********SYSTEM WIN*********")
      break
 else:#if no one win then repeat the loop
            args=["S","K","Q"]
            a=random.choice(args) #system choice
            print(f"round={i}")#showing the number of the rounds
            b=input("Please input S or K or Q:")#user choice
            b=b.upper()#for user to input (s or S)(k or K)(q or Q) not gonna be a problem
            while b=="Q" or b=="S"or b=="K" :#while loop for the main game

                if   b==a :#statements of the game
                                
                    print("^^^^^^^^Draw^^^^^^^^^")
                    break
                                
                                                            
                elif (a=="S" and  b=="K") or (a=="Q" and b=="S") or (a=="K" and b=="Q"):
                                
                    print("&&&&&&User Win&&&&&&&") 
                    winu+=1        
                    break
                                                            
                else :
                    print("$$$$$$$User Lost$$$$$$$$")  
                    winc+=1
                    break
            print(f"system choice was {a}")#print system choice for user
          
            

