# #------------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------------------------------------
##                                              Concepts in python

#       #       rstrip

def str_strip():
    txt = ".,.,.,.,.,.banana,,,,,ssqqqww....."
    x = txt.rstrip(",.qsw")
    print('Explanation:')
    print('rstrip takes whatever trailing chars(the end ones) and removes it/them')
    print("it is not limited to 1 character at a time, since it doesn't treat it has a whole string rather as individual chars\n")

    print('Example:')
    print(f'start string: "{txt}" and what we want removed is: ,.qsw')
    print(x)
##<<<<<<<<<<<.,.,.,.,.,.banana

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       ord & chr

def str_ord_chr():
    print('Explanation:')
    print('ord takes unicode char any turns it into a number\n')
    
    print('Example:')
    character = 'P'
    unicode_char = ord(character)
    print(f'ord for "P" is: {unicode_char}')
##or: print(ord('P'))
##<<<<<<<<<<<<80

    print('\n\nExplanation:')
    print('chr takes a number and turns it into a unicode char\n')

    print('Example:')
    print(f'chr for 97 is: {chr(97)}')
    print(f'chr for 98 is: {chr(98)}')
##<<<<<<<<<a
##<<<<<<<<<b

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Swapcase

def str_swapcase():
    print('Explanation:')
    print('swaps upper and lower case letters in a string\n')

    print('Example:')
    txt = "Hello How ArE you TODAY?"
    x = txt.swapcase()
    print(f'Orginal string: {txt}')
    print(f'After swapped case: {x}')
    ##<<<<<<<<<<<hELLO hOW aRe YOU today?

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Substring

# syntax: string[start:end:step]

def str_substring():
    print('Example 1:')
    print(f'Get first 5 chars from: freeCodeCamp')
    string = "How Are you doing?"
    #[0:5] is the same as [:5]
    print(string[:5])
##<<<<<<<<<<<How A

    print('\n\nExample 2:')
    print(f'Get 4 chars starting from 3rd char (index starts at 0)')
    string = "How Are you doing?"
    print(string[2:6])
##<<<<<<<<<<<W Ar

    print('\n\nExample 3:')
    print(f'Get last char')
    string = "How Are you doing?"
    print(string[-1])
    print(f'\n:-1 is everything else other than the last char')
##<<<<<<<<<<<?

    print('\n\nExample 4:')
    print(f'every other char')
    string = "How Are you doing?"
    print(string[::2])
##<<<<<<<<<<<HwAeyudig

    print('\n\nExample 5:')
    print(f'reverse the string')
    string = "How Are you doing?"
    print(string[::-1])
##<<<<<<<<<<<?gniod uoy erA woH

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Count and Length

def str_count_length():
    print('Explanation:')
    print('Count can count the number of times a certain letter/substring is in a string')
    print('Length gets you the length of the whole string, or a substring.\n')

    print('Example:')
    message = 'How are you doing on this fine day?'
    print(f'Orginal string: {message}')
    print(f'Number of times o is in the string: {message.count("o")}')
    print(f'Length of the string: {len(message)}')
    print(f'Length of the first 5 chars: {len(message[0:5])}')
##<<<<<<<<<<<Output

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       find, startwith and endswith

def find_start_end():
    print('Explanation:')
    print('find: before using find check if the substring is in the string, find finds the position that the substring is at')
    print('startswith: returns True or False if it starts with the substring given')
    print('endswith : returns True or False if it ends with the substring given\n')

    print('Example:')
    test = 'How You doing?'
    print(f'Orginal string: {test}\n')
    print(f'Where is "You" in the string: {test.find("You")}')
    print(f'Does string start with H? {test.startswith("H")}')
    print(f'Does string end with H? {test.endswith("H")}')
##<<<<<<<<<<<Output
##<<<<<<<<<<<Output
##<<<<<<<<<<<Output

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       different str.is[something]

def str_is():
    print('Explanations:')
    print('str.isalpha returns True if all chars is [a-z] and there is at least 1 char')
    print('str.isdecimal returns true if all is [0-9] where str.isdigit also considers something like ² as true')
    print('str.upper and str.lower converts the string to upper or lower')
    print('str.isupper and str.islower: checks if whole string(or substring) is lower or upper case')
    print('str.isspace checks if whole string(or substring) is all whitespaces')
    print('str.replace(old, new)')
    
# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       abs

def num_abs():
    print('Explanation:')
    print('Gives the absolute number, can be used with int, float and complex numbers.\n')

    print('Example:')
    print(f'abs of -20: {abs(-20)}')
    print(f'abs of -4.5: {abs(-4.5)}')
##<<<<<<<<<<<Output

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       math imports
import math

def num_rounding():
    print('Explanation:')
    print('math.floor(num) and math.ceil(num) rounds the number either up or down to the whole number\n')
    print('round(num) rounds down or up to the nearest whole number')

    l = [1.5,2.2,3.6,4.9,5.05,6.1]
    for i in l:
        print(f'Number being handled: {i}')
        print(f'round: {round(i)}')
        print(f'floor: {math.floor(i)}')
        print(f'ceil: {math.ceil(i)}')

##<<<<<<<<<<<Output

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Number to binary converter

def add_binary(a, b):
    print('From Number to binary')
#   {} - makes it into a string
#   a+b - adds the 2 numbers together
#   :b - formats it as a binary number
    print(f'numbers: {a}, {b}')
    print(f'{a+b:b}')
##<<<<<<<<<<<1011

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       regex
#alt står her: https://www.w3schools.com/python/python_regex.asp
#basic email finder
#(\S+\@\S+)
#email finder, but finds the email in the last group, 
#and sets all text before it in another group, and anything after the email will not be found, 
#unless another mail is after the next text. And only works when something  like: "x@x" sign is present.
#((?:[^\n]+?\n)*?)(\S+?\@\S+)


import re
def regex():
    teststring = '''Hej med dig!
                   72 år gammel Bent.'''
    #\w*\w[\w*\w!.] find correct, but maybe a bit long
    #\w*\W finds all, but with a new line, and tab spaces if introduced
    #\w*\W\S+ finds all, but groups "Hej" and "med" together
    #\S+ finds all, and leaves them seperate, as the first one
    patteren = '\S+'
    x = re.findall(patteren, teststring)
    print(x)
    print('\n\nLook at code comments')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Tuple

def coll_tuple():
    #Tuple bliver brugt til at gemme på flere items i en variable, og den kan ikke laves om på når den først er lavet og tillader duplicates
    mytuple = ("Car", "Plane", "Ship")
    print(f'mytuple: {mytuple}')
    print(f'type of mytuple: {type(mytuple)}')
    thistuple = ("apple",)
    print(f'thistuple: {thistuple}')
    print(f'type of thistuple: {type(thistuple)}')
    #Ikke en tuple husk komma til sidst.
    thistuple = ("apple")
    print(f'new thistuple: {thistuple}')
    print(f'type of the new thistuple: {type(thistuple)}') 
    print('Remember the "," after the element in the tuple, else it will be a string')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       List

def coll_list():
    #Lister er sat i en bestemt rækkefølge(kan laves om på med nogle methods), kan laves om på efter de er lavet og tillader duplicates
    mylist = ["Car", "Plane", "Ship"]
    print(f'mylist: {mylist}')
    print(f'type of mylist: {type(mylist)}')
    print(f'Add on at the end of the row:')
    mylist.append(32)
    print(f'new mylist: {mylist}')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Set

def coll_set():
    #Sets er ikke i en rækkefølge, du kan ikke ændre på dem(andet end at fjerne og tilføje items) og tillader ikke nogle duplicates
    myset = {"Car", "Plane", "Submarine", "Ship"}
    print(myset)
    print(type(myset))
    #True og 1 bliver set som samme value, samme med False og 0
    thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
    print(thisset)

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Dict

def coll_dict():
    #Dictionaries bliver brugt til at gemme på key:value pairs, dictionaries har en rækkefølge, kan laves om på og tillader ikke duplicates
    thisdict =	{
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(thisdict)
    print(type(thisdict))

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Enumerator

def enumerator():
    #enumerate takes a object and either takes it from letter to letter and kinda assigns a number to each with a list(can most likely be used with other things)
    
    #test string
    s1 = "geekdpi"
    #list variable where we will append to with the various letters
    out = []
    print(list(s1))
    #for show about how enumerate works and why we can have 2 variables with it in the for-loop
    print(list(enumerate(s1)))
    #it makes a count for each letter: g-0 e-1 e-2 k-3 d-4 p-5 i-6 and takes the number and says fx: 1*6=6, so 6 extra lowercase i and the one uppercase from the start. 
    #Then you join a - on the out vairable, which means you get the correct number and format for the codewars problem Mumbling(kata 7)
    for count, letter in enumerate(s1):
        out.append(letter.upper() + letter.lower()*(count))
    print('-'.join(out))
    

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Map

def maps():
    # Understanding - its syntax is map(function, iterable). The function doesn't need to be a function.
    #But can be something like list, int, string... you can do it like that to convert something to your desired type
    #1st example is of it using a fucntion and then adding 2 variables together, 2nd example is of converting from string to int, and then formatting it into a string again.

    def myfunc(a, b):
      return a + b

    x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

    print(x)

    #convert the map into a list, for readability:
    print(list(x))




    #def high_and_low(numbers):    
    #    digits = list(map(int, numbers.split(' ')))
    #    low = min(digits)
    #    high = max(digits)

    #    return ('{} {}'.format(high, low))
    ##     string below does the same thing without the low and high variables.
    ##     return ('{} {}'.format(max(digits), min(digits)))
    #high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4')
    #pass


# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       3 if return statements

def return_statement():
    print('Explanation:')
    print('this can get 3 if else statements, normal example:\n')
    print('''if x < 2: return x
             elif x >= 2 and x < 10: return x
             else: return x''')

    print('Example/The way to do it in 1 line:')
    print(f'return n*100 if n < 5 else n*95 if n>= 5 and n < 10 else n*90')
    print('The statement is split up like this:')
    print('return n*100 if n < 5 ||| else n*95 if n>= 5 and n < 10 ||| else n*90')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       split a multiple words string into multiple different list's to handle it

def split_list():
    text = 'hej med dig jeg hedder kaj'
    print('string til at starte med: hej med dig jeg hedder kaj')
    for word in text.split():
        # turn word into a list
        word = list(word)
        print(word)

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       split a multiple words string into multiple different list's to handle it

def str_to_int_list():
    size = 5
    count = 1
    res = []
    while(count <= size):
        res += str(count)
        count += 1
    #it is eval that does the converting to int, cant be done with int(var)
    res = [eval(i) for i in res]
    print(res)

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       get the name of a url out with regex

def url():
    import re
    patteren = ''
    url = 'https://www.google.com'
    #if there is a www in the url, then we cant just take only the first element
    if 'www' in url:
        patteren = '(\w+.*?)'
        x = re.findall(patteren, url)
        #match group here is 3rd, where if no https present its 2nd
        if url[0] == 'h':
            return x[2]
        #2nd match group used
        else:
            return x[1]
    #if there is https present
    elif url[0] == 'h':
        patteren = '/\/+(.*?)[\^.]'
        x = re.findall(patteren, url)
        return x[0]
    #if there is neither https or www present in the url.
    else:
        patteren = '(\w+.*?)'
        x = re.findall(patteren, url)
        return x[0]



from os import system

def main():
    loop = True
    while loop == True:
        print('Enter what you want to take a look at: ')
        x = input().lower()
        ##os.system('clear') - works on bash(something like linux) or macOSX systems
        ##os.system('clr') - works only on windows
        system('clear')
        match x:
            #-------------------------------------------
            #strings
            case 'rstrip':
                str_strip()
            case 'ord_chr':
                str_ord_chr()
            case 'swapcase':
                str_swapcase()
            case 'substring':
                str_substring()
            case 'count_length':
                str_count_length()
            case 'find_start_end':
                find_start_end()
            case 'str_is':
                str_is()
            case 'split_list':
                split_list()
            #-------------------------------------------
            #numbers
            case 'abs':
                num_abs()
            case 'rounding':
                num_rounding()
            case 'binary':
                add_binary(3, 8)
            #-------------------------------------------
            #regex
            case 'regex':
                regex()
            #-------------------------------------------
            #Collections
            case 'tuple':
                coll_tuple()
            case 'list':
                coll_list()
            case 'set':
                coll_set()
            case 'dict':
                coll_dict()
            #-------------------------------------------
            #Enumerator
            case 'enumerator':
                enumerator()
            #-------------------------------------------
            #Map
            case 'map':
                maps()
            #-------------------------------------------
            #strings in list to ints
            case 'str_to_int_list':
                str_to_int_list()
            #-------------------------------------------
            #find url names with regex
            case 'url':
                url()
            #-------------------------------------------
            #3 if statements in 1 return example
            case '3_return_statement':
                return_statement()
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
        print('\nDo you want to Continue? [y/n]')
        y_n = input().lower()
        if y_n == 'n':
            loop = False
        else:
            loop = True

if __name__ == "__main__":
    main()


#Template:

#       #       [Name]

def Name():
    print('Explanation:')
    print('Something Something\n')

    print('Example:')
    print(f'Something Something')
    print(f'Something Something')
##<<<<<<<<<<<Output

# #------------------------------------------------------------------------------------------------------------------------------------------------
