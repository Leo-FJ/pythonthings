'''
A decorator is a special type of function that is used to modify the behavior of another function.
Decorators allow you to wrap another function, 
adding functionality before or after the wrapped function is executed. 
They provide a convenient way to extend or modify the behavior of functions 
without changing their code directly.
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''Output:
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
'''



###Another Example

def sorted_list_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return sorted(result)
        else:
            raise TypeError("The result must be a list.")
    return wrapper

@sorted_list_decorator
def add_and_sort_list(list1, list2):
    result = list1 + list2
    #First print statement
    print("Function executed.")
    print(f'lists unsorted(before decorator): {result}')
    #returns everything into the decorator, and executes whats in the decorator
    return result

result = add_and_sort_list([3, 1, 4], [1, 5, 9])
#second print statement, after the decorator has been executed
print("Result after decorator:", result)
'''
Function executed.
lists unsorted(before decorator): [3, 1, 4, 1, 5, 9]
Result after decorator: [1, 1, 3, 4, 5, 9]
'''



########################################################
'''
Class objects, you can put a thing like a string into a function/method
and of course manipulate that string/variable how you want to.
'''

def shout(text):
  return text.upper()

print(shout('How you doing?')

'''Output:
HOW YOU DOING?
'''
