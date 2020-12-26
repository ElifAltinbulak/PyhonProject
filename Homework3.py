#Homework3
import random as rnd
picture=["""
+-------+
    |   |
    0   |
        |
        |
        |
  ------+""",
"""
+-------+
    |   |
    0   |
    |   |
        |
        |
  ------+""",
"""
+-------+
    |   |
    0   |
   /|   |
        |
        |
  ------+""",
"""
+-------+
    |   |
    0   |
   /|\  |
        |
        |
  ------+""",
"""
+-------+
    |   |
    0   |
   /|\  |
   /    |
        |
  ------+""",
"""
+-------+
    |   |
    0   |
   /|\  |
   / \  |
        |
  ------+
"""]
al = ["tiger","snake","shark"]
f1 = ["olive","honey","bread"]
fl1= ["daisy","lotus","tulip"]
new =["","","","",""]
print("-_-_-HANGMAN-_-_-")
name = input("What is your name? :")
print(f"Welcome, {name.capitalize()}")
print("!!!!The rule of the game: 1 right on every wrong GOOD LUCK :)!!!!")
c = int(input("1-Foods\n2-Flowers\n3-Animals\n**Please,select a category : "))
if c==1:
    print("*******FOODS******")
    sf =list(rnd.choice(f1))
    step = 6
    while True:
        word=input("Enter the one word: ")
        if word.isalpha()==True:
            word=word.lower()
            if word in sf:
                food=sf.index(word)
                new.insert(food,word)
                new.pop(food+1)
                print(new)
                if (list(new)==list(sf)):
                    print("YOU WİN!!")
                    break
            else:
                step-=1
                print(f"Right: {step}")
                print("You guessed wrong!")
                if step==5:
                    print(picture[0])
                elif step==4:
                    print(picture[1])
                elif step==3:
                    print(picture[2])
                elif step==2:
                    print(picture[3])
                elif step==1:
                    print(picture[4])
                elif step==0 and picture[5]:
                    print(picture[5])
                    print(f"GAME OVER!:( >>{sf}<<")
                    break
        else:
            print("Enter the one word: ")
            continue
elif c==2:
    print("*******FLOWERS*******")
    sfl1 =list(rnd.choice(fl1))
    step = 6
    while True:
        word=input("Enter the one word: ")
        if word.isalpha()==True:
            word=word.lower()
            if word in sfl1:
                flower=sfl1.index(word)
                new.insert(flower,word)
                new.pop(flower+1)
                print(new)
                if (list(new)==list(sfl1)):
                    print("YOU WİN!!")
                    break
            else:
                step-=1
                print(f"Right: {step}")
                print("You guessed wrong!")
                if step==5:
                    print(picture[0])
                elif step==4:
                    print(picture[1])
                elif step==3:
                    print(picture[2])
                elif step==2:
                    print(picture[3])
                elif step==1:
                    print(picture[4])
                elif step==0 and picture[5]:
                    print(picture[5])
                    print(f"GAME OVER!:( >>{sfl1}<<")
                    break
        else:
            print("Enter the one word: ")
            continue
elif c==3:
    print("*******ANIMALS*******")
    sal =list(rnd.choice(al))
    step = 6
    while True:
        word=input("Enter the one word: ")
        if word.isalpha()==True:
            word=word.lower()
            if word in sal:
                anımal=sal.index(word)
                new.insert(anımal,word)
                new.pop(anımal+1)
                print(new)
                if (list(new)==list(sal)):
                    print("YOU WİN!!")
                    break
            else:
                step-=1
                print(f"Right: {step}")
                print("You guessed wrong!")
                if step==5:
                    print(picture[0])
                elif step==4:
                    print(picture[1])
                elif step==3:
                    print(picture[2])
                elif step==2:
                    print(picture[3])
                elif step==1:
                    print(picture[4])
                elif step==0 and picture[5]:
                    print(picture[5])
                    print(f"GAME OVER!:( >>{sal}")
                    break
        else:
            print("Enter the one word: ")
            continue

   
    
                      
    
    
    
            
        
                
                
    


            

            
    
    
