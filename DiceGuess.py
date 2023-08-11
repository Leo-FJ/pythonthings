import random
import os

def main():
    while(True):
        os.system('cls')
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        number = dice1+dice2

        guess = int(input('Guess the number that the 2 dice will be: '))
        if(guess == number):
            print('Congratulations! you won')
        else:
            print('Im sorry, but you lost')
            print('the number was: ', number)
        
        #there is most likely a better way to do it
        #just there to see if you input either an y or n
        while(True):
            again = str.lower(input('\nWant to try again= [y/n]'))
            if(again == 'y'):
                break
            elif(again == 'n'):
                break
            else:
                print('try inputting a "y" or a "n"')

        #says if the outer loop should continue
        if(again == 'y'):
            continue
        elif(again == 'n'):
            break

if __name__ == "__main__":
    main()
