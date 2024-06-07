## Guess The Number  

print ("Welcome To The Number Guessing Game")
print("I am thinking of a number between 1 to 100 ")  
print("Which level You Want ?") 
level1=input("Easy or Hard ? ") 
Actual_Number= 40 
if level1 == "Easy":
    for i in range(1,11):
        Guess_The_Number=int(input("Guess The Number "))
        if Guess_The_Number <= 100:
            if Guess_The_Number==Actual_Number:
                print("Correct !! You Won The Game ") 
            elif Guess_The_Number >= 45:
                print("Wrong!! .You Are Too High ")
                print(f"You have {10-i} choice left  ") 
            elif Guess_The_Number <= 35 :
                print("Wrong!! .You Are Too Low ")
                print(f"You have {10-i} choice left  ")
            else :
                print("wrong") 
                print(f"You have {10-i} choice left  ")
            if i ==10:
                print("GAME OVER !! . You've Lost The Game") 
        else:
            print("Take The Number Between 1 to 100 ") 
             
if level1=="Hard":
    for i in range(1,6):
        Guess_The_Number=int(input("Guess The Number "))
        if Guess_The_Number <= 100:
            if Guess_The_Number==Actual_Number:
                print("Correct !! You Won The Game ")
                break
            elif Guess_The_Number >= 45:
                print("Wrong!! .You Are Too High ")
                print(f"You have {5-i} choice left  ") 
            elif Guess_The_Number <= 35 :
                print("Wrong!! .You Are Too Low ")
                print(f"You have {5-i} choice left  ")
            else:
                print("wrong") 
                print(f"You have {5-i} choice left  ")
        else:
            print("Take The Number Between 1 to 100 ")
        if i == 5:
            print("GAME OVER !! . You've Lost The Game") 


