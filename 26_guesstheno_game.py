import random
target= random.randint(1,100)


while True:
 user_choice= input("Enter any number or Quit")
 if(user_choice=="Quit"):
    break
 user_choice = int(user_choice)

 if(user_choice==target):
   print("Your guess is correct!!!")
   break
 elif(user_choice<target):
   print("Your number is too small.... take a bigger guess")
 else:
   print("Your number is too big.... take a smaller guess")

print("------Game Over------")

 
