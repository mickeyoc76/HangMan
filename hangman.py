import random

def new_game():
        
    new_game = input("play another y/n? ")
    if new_game[0].lower() == 'y':
        return "y"
    else:
        return "n"

def hman():
    
    Playing = True
    while Playing:  
        
        with open('words.txt') as f:
            words = list(f)
            choice = random.choice(words).strip().lower()
            answer = []
            for dash in choice:
                answer.append("_")
            print("Your word has %d letters" %(len(answer)))
        
            count = 10    
            while count <= 10:        
                print("You have %d attempts to guess the word" %(count))
                choose = input("Enter a letter: ")
                for i,l in enumerate(choice):
                    if choose in l: 
                        answer[i] = l
                        print(answer)
                if answer == list(choice):
                    print("Winner! ")
                    answer = new_game()
                    if answer == 'y':
                        break
                    else:
                        Playing = False
                        print("Game Over!")
                        break
                elif count == 0:
                    print("You have run out chances, the word was %s! " %(choice))
                    answer = new_game()
                    if answer == 'y':
                        break
                    else:
                        Playing = False
                        print("Game Over!")
                        break
                else:
                    count -= 1
                    continue
hman()


