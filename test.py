# #------------------------------------------------

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
    
# #------------------------------------------------    
    
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
    
# #------------------------------------------------

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
    
# #------------------------------------------------

#       #       Noget med classer, Class
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age) 

# #------------------------------------------------

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
 
# #------------------------------------------------

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

# #------------------------------------------------

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

# #------------------------------------------------

#       #       import og datetime
# import datetime
## import datetime as time

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%c"))
#%a dagen i kort form, %A fuld version af dagen, 
#%d dagen af måneden
#%b kort version af måneden, %B fuld version af måneden
#%Y fulde år, %y kort år fx: 2018 bliver til 18
#%H timen, %M minut, %S sekund, %Z tidszone, 
#%j dag af året, %W uge nr(mandag første dag)
#%c dag, måned, klokken, år

# #------------------------------------------------

#       #       regex
#alt står her: https://www.w3schools.com/python/python_regex.asp






# def main():
#     pass

# if __name__ == "__main__":
#     main()
