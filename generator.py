# #Random Password generator
import os
import string
import random
import time

def main():
    while(True):
        #clears screen
        os.system('cls')
        #gives us the length of the password
        try:
            length = int(input('How long do you want the password: '))
            print('''Choose which character sets you want from this list, input their number to choose them
                  1. Digits
                  2. Letters
                  3. Special characters
                  4. Get Passsword with my choices''')

            characters = ''
            #choices in what your password should contain
            while(True):
                choice = int(input('Write Your number: '))
                if(choice == 1):
                    #gives numbers
                    characters += string.digits
                elif(choice == 2):
                    #gives normal letters
                    characters += string.ascii_letters
                elif(choice == 3):
                    #gives special characters
                    characters += string.punctuation
                elif(choice == 4):
                    break
                else:
                    print('Something went wrong, try again')
                    
                password = []
    
            for i in range(length):
                randomchar = random.choice(characters)
    
                password.append(randomchar)
    
            print(f'Your password is: ' + ''.join(password))
            
            #just there to see if you input either an y or n
            while(True):
                again = str.lower(input('Want to try again= [y/n]'))
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
        except:
            print('try again, it will start again in 5')
            time.sleep(5)
            main()
            
if __name__ == "__main__":
    main()
