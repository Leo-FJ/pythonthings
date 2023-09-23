# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Anagram, input og sorted
# def Anagram():
#     #for de forskellige strings
#     anagram1 = input('Anagram 1:\n')
#     anagram2 = input('Anagram 2:\n')
#     #sortere dem for at de har en chance for at stå i samme rækkefølge
#     sorted1 = sorted(anagram1)
#     sorted2 = sorted(anagram2)
    
#     #checker om de er det samme
#     if(sorted1 == sorted2):
#         print('Det er rigtigt')
#     else:
#         print('det er forkert')
    
# #------------------------------------------------------------------------------------------------------------------------------------------------
    
#       #       Convert Celsius to Fahrenheit, try and exception
# def Celsius():
#     #får grader i Celsius
#     Celsius = input('temperaturen\n')
#     #try expect på om de har skrevet et tal eller andet, 
#     #hvis et tal går det igennem rigtigt og giver dig hvad du forventer
#     #ellers får du en besked om noget gik forkert.
#     try:
#         Fahrenheit = round((1.8 * int(Celsius)) + 32, 2)
#         print(f'Du gav {Celsius} grader og det er {Fahrenheit} i Fahrenheit')
#     except:
#         print('Du skrev nok noget forkert, prøv igen')
    
# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       FizzBuzz, Loops og Conditions
# def FizzBuzz():
#     for x in range(20):
#         if(x % 3 == 0 and x % 5 == 0):
#             print('FizzBuzz')
#             #continue fordi så tjekker den ikke resten for det tal
#             continue
#         elif(x % 3 == 0):
#             print('Fizz')
#             continue
#         elif(x % 5 == 0):
#             print('Buzz')
#             continue
#         else:
#             print(x)
    
# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Noget med classer, Class
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age) 

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Mere med classer, Function in class
# class Person():
#     def __init__(self, Name, Age, Country):
#         self.Name = Name
#         self.Age = Age
#         self.Country = Country
    
#     def Introduction(self):
#         print(self.Name)
#         print(self.Age)
#         print(self.Country)
        
# People = Person('Bodil', 72, 'Denmark')
# People.Introduction()
 
# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Class inheritance
#       #   Første eksempel:  
# class City():
#     def __init__(self, city):
#         self.city = city

# class Person(City):
#     def __init__(self, Name, Age, Country, city):
#         self.Name = Name
#         self.Age = Age
#         self.Country = Country
#         self.city = city
    
#     def Introduction(self):
#         print(self.Name)
#         print(self.Age)
#         print(self.Country)
#         print(self.city)
        
# People = Person('Bodil', 72, 'Denmark', 'København')
# People.Introduction()

#       #   Andet eksempel:
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Jakob", "Olsen")
# x.printname()

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Class Polymorphism
#       #   Første eksempel:  
# class Car():
#     def __init__(self, brand, name, year: int):
#         self.brand = brand
#         self.name= name
#         self.year = year
    
#     def move(self):
#         print('Driving')
        
# class Plane():
#     def __init__(self, brand, name, year: int):
#         self.brand = brand
#         self.name= name
#         self.year = year
    
#     def move(self):
#         print('Flying')
        
# class Ship():
#     def __init__(self, brand, name, year: int):
#         self.brand = brand
#         self.name= name
#         self.year = year
    
#     def move(self):
#         print('Sailing')
        
# car1 = Car("Audi", "A8", 4)
# ship1 = Ship("Ibiza", "Touring 20", 35)
# plane1 = Plane("Boeing", "747", 15)

# for x in (car1, ship1, plane1):
#     x.move()

#       #   Andet eksempel:
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")
# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Class variables, classmethod
#import random

#class Hat:
#    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
#
#    @classmethod
#    def sort(cls, name):
#        print(f'{name} is in {random.choice(cls.houses)}')
#
#Hat.sort('Ron')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       import og datetime
# import datetime
# # import datetime as time

# x = datetime.datetime(2018, 6, 1)

# # print(x.strftime("%c"))
# #%a dagen i kort form, %A fuld version af dagen, 
# #%d dagen af måneden
# #%b kort version af måneden, %B fuld version af måneden
# #%Y fulde år, %y kort år fx: 2018 bliver til 18
# #%H timen, %M minut, %S sekund, %Z tidszone, 
# #%j dag af året, %W uge nr(mandag første dag)
# #%c dag, måned, klokken, år

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       regex
# #alt står her: https://www.w3schools.com/python/python_regex.asp
# #basic email finder
# #(\S+\@\S+)

# #email finder, but finds the email in the last group, 
# #and sets all text before it in another group, and anything after the email will not be found, 
# #unless another mail is after the next text. And only works when something  like: "x@x" sign is present.
# #((?:[^\n]+?\n)*?)(\S+?\@\S+)


#import re

#teststring = '''Hej med dig!
#               72 år gammel Bent.'''
# #\w*\w[\w*\w!.] find correct, but maybe a bit long
# #\w*\W finds all, but with a new line, and tab spaces if introduced
# #\w*\W\S+ finds all, but groups "Hej" and "med" together
# #\S+ finds all, and leaves them seperate, as the first one
# #patteren = '\S+'
#x = re.findall(patteren, teststring)
#print(x)

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Collections (Arrays) --> List, Tuple, Set, Dictionary
#   #   Tuple
# #Tuple bliver brugt til at gemme på flere items i en variable, og den kan ikke laves om på når den først er lavet og tillader duplicates
# mytuple = ("Car", "Plane", "Ship")
# print(mytuple)
# print(type(mytuple))

# thistuple = ("apple",)
# print(type(thistuple))
# #Ikke en tuple husk komma til sidst.
# thistuple = ("apple")
# print(type(thistuple)) 

#   #   List
# #Lister er sat i en bestemt rækkefølge(kan laves om på med nogle methods), kan laves om på efter de er lavet og tillader duplicates
# mylist = ["Car", "Plane", "Ship"]
# print(mylist)
# print(type(mylist))
# #Tilføjer en ny bagerst i rækken.
# mylist.append(32)
# print(mylist)

#   #   Sets
# #Sets er ikke i en rækkefølge, du kan ikke ændre på dem(andet end at fjerne og tilføje items) og tillader ikke nogle duplicates
# myset = {"Car", "Plane", "Submarine", "Ship"}
# print(myset)
# #True og 1 bliver set som samme value sammed med False og 0
# thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
# print(thisset)

#   #   Dictionaries
# #Dictionaries bliver brugt til at gemme på key:value pairs, dictionaries har en rækkefølge, kan laves om på og tillader ikke duplicates
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Map

# Understanding - its syntax is map(function, iterable). The function doesn't need to be a function.
#But can be something like list, int, string... you can do it like that to convert something to your desired type
#1st example is of it using a fucntion and then adding 2 variables together, 2nd example is of converting from string to int, and then formatting it into a string again.

# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)

# convert the map into a list, for readability:
# print(list(x))




# def high_and_low(numbers):    
#     digits = list(map(int, numbers.split(' ')))
#     low = min(digits)
#     high = max(digits)
    
#     return ('{} {}'.format(high, low))
#     #string below does the same thing without the low and high variables.
#     #return ('{} {}'.format(max(digits), min(digits)))
# high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4')

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Enumerator

#enumerate takes a object and either takes it from letter to letter and kinda assigns a number to each with a list(can most likely be used with other things)

##test string
# s1 = "geekdpi"
##list variable where we will append to with the various letters
# out = []
# print(list(s1))
##for show about how enumerate works and why we can have 2 variables with it in the for-loop
# print(list(enumerate(s1)))
##it makes a count for each letter: g-0 e-1 e-2 k-3 d-4 p-5 i-6 and takes the number and says fx: 1*6=6, so 6 extra lowercase i and the one uppercase from the start. 
##Then you join a - on the out vairable, which means you get the correct number and format for the codewars problem Mumbling(kata 7)
# for count, letter in enumerate(s1):
#     out.append(letter.upper() + letter.lower()*(count))
# print('-'.join(out))

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       Number to binary converter

#def add_binary(a,b):
#    # {} - makes it into a string
#    # a+b - adds the 2 numbers together
#    # :b - formats it as a binary number
#    return f'{a+b:b}'

#print(add_binary(3,8))

# #------------------------------------------------------------------------------------------------------------------------------------------------

#       #       import string

#import string

#sentence = 'Hey, how are you doing today?'

#sentence_capatalized = sentence.capwords

#print(sentence_capatalized)


# if __name__ == "__main__":
#     main()


##import os
##os.system('clear') - works on bash(something like linux) or macOSX systems
##os.system('clr') - works only on windows
