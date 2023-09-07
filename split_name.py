import sys
import os

def main():
    os.system('clear')
    #takes both names as input, and removes all whitespace
    names_input = input('Skriv 2 navne som: navn,navn: ').replace(' ', '')
    #makes names the return value of split function
    names = split_name(names_input)
    print(names, sep='\n')

#function to split the name string where there is a , seperator.
def split_name(names_input):
    #counts if the string names_input has more than 1 ",", and if so we exit
    count = names_input.count(',')
    if(count == 1):
        #replacing "," with a newline
        s = ''.join(names_input.replace(',','\n'))
    else:
        sys.exit('For mange navne')

    return s

if __name__ == '__main__':
    main()
