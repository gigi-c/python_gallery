# 1. VARIABLES AND TYPES
# 1a. support two types of numbers: integers and float
int_number = 7
float_number = 7.0
print(type(int_number))
print(type(float_number))
  # change integer to float and float to integer
to_float_number = float(int_number)
to_int_number = int(float_number)
print(to_float_number)
print(type(to_float_number))
print(to_int_number)
print(type(to_int_number))
# 1b. strings
string_variable = "hello"
print(type(string_variable))
# operators can be executed on numbers and strings
x = 1
y = 2
a = "hello"
b = "world"
print (x + y)
print(a + " " + b)
print(x + a) # WILL NOT WORK
# 1c. booleans: ouput will be TRUE or FALSE (refer to CONDITIONS)
print(10 > 9)
print(10 == 9)
print(10 < 9)

# 2. COLLECTIONS
# 2a. List: a collection which is ORDERED and CHANGEABLE (allow duplicate members)
names_list = ["WanChi", "Weiyee", 'CJ', "Andy", "Ben", "Jonny", "Yin", "Shugs", "Vijay"]
    # accessing items in the list by using index which start with 0
second_name = names_list[1]
last_name = names_list[-1] # negative index means beginning from the end of the list, starts with -1
third_to_sixth_name = names_list[2:6] # range index specify where to begin and where to end (output is a new list)
print(second_name)
print(last_name)
print(third_to_sixth_name)
    # change item in the list
names_list[0] = "Gigi"
print(names_list)
    # determine number of items in the list
list_length = len(names_list)
print(list_length)
    # add item into the list
names_list.append("Don") # add to the end of the list
print(names_list)
names_list.insert(3, "Joyce") # specify the position to add the item
print(names_list)
    # delete item in the list
names_list.remove("Joyce")
print(names_list)
names_list.pop() # remove the last item if index is not specified
print(names_list)
# 2b. Tuple: a collection which is ORDERED and UNCHANGEABLE (allows duplicate members)
#            CANNOT add or delete item from tuple since tuple is UNCHANGEABLE
names_tuple = ("Gigi", "Weiyee", 'CJ', "Andy", "Ben", "Jonny", "Yin", "Shugs", "Vijay")
    # access item in tuple using index
first_name = names_tuple[0]
print(first_name)
    # number of items in tuple
tuple_length = len(names_tuple)
print(tuple_length)
# 2c. Set: a collection which is UNORDERED and UNINDEXED (no duplicate members)
#          CANNOT access set using index
names_set = {"Gigi", "Weiyee", 'CJ', "Andy", "Ben", "Jonny", "Yin", "Shugs", "Vijay"}
print(names_set) # may not be the same order as the input
print(len(names_set)) # number of items in the set
    # add item into the set
names_set.add("Don") # add one item
print(names_set)
print(len(names_set))
names_set.update(["Joyce", "Mark"]) # add multiple items
print(names_set)
print(len(names_set))
    # remove an item in the set
names_set.remove("Don")
print(names_set)
names_set.pop() # remove the last item (set is unorder so will not know which item is being removed)
print(names_set)
# 2d. Dictionary: a collection which is UNORDERED, CHNAGEABLE and INDEXED (no duplicate members)
#                 containts KEYS and VALUES
sparta_dict = {"stream": "Data 9",
               "trainer": "Isabella",
               "number of trainees": 11}
    # accessing item using key
stream = sparta_dict["stream"]
print(stream)
     # change values
sparta_dict["number of trainees"] = 9
print(sparta_dict)
     # adding item
sparta_dict["start date"] = ["24 Feb 2019"]
print(sparta_dict)
    # remove item using key name
sparta_dict.pop("start date")
print(sparta_dict)

# 3. CONDITIONS (can be use with control flow or booleans)
x == y # equals to
x != y # not equals to
x < y # less than
x <= y # less than or equal to
x > y # greater than
x >= y # greater than or equal to

# 4. CONTROL FLOW
# 4a. If....Else: if statements are executed from top down
#                 as soon as one of the conditions controlling the if is true, the associated statement is executed
#                 if none of the conditions is true, final else statement will be executed
num1 = 10
num2 = 30
if num1 < num2:
    print("{} is smaller than {}".format(num1, num2))
elif num1 > num2:
    print("{} is greater than {}".format(num1, num2))
else:
    print("the two numbers equal to each other")
# 4b. For loop: use to iterate over a sequence
for number in range(6): # range starts with 0 and end with the number-1
    print("number is now", number)
    # Nested loop: a loop inside a loop
adj = ["red", "massive", "tasty"]
fruits = ["apple", "banana", "pear"]
for x in adj:
    for y in fruits: # inner loop is executed one time for each iteration of the outer loop
        print(x, y)
    # CONTINUE statement: skip the processing of the rest of the loop for the current iteration
numbers = [12, 16, 17, 24, 29, 30]
for i in numbers:
    if i%2 == 1: # if the number is odd
        continue # do not process it (print)
    print(i)
print("end of loop")
    # BREAK statement: leave the loop immediately and execute the rest of the statments outside the loop
for i in numbers:
    if i%2 == 1: # if the number is odd
        break    # exit the loop immediately
    print(i)
print("end of loop")
# 4c. While loop: execute an unknown number of times as long as the BOOLEAN expression is TRUE
#     Flow of execution: 1. evaluate the boolean expression, yielding TRUE or FALSE
#                        2. if false, exit the while loop and continue execution in the next statement
#                        3. if true, execute each statements within the while loop then go back to step 1
i = 1
while i < 10: # as long as i is less than 10,
   print(i)   # i is printed
   i += 1     # i now becomes i + 1, then run the while loop again
else: # when the while condition become false, the else statement is executed
    print("i is no longer less than 10")
    # can use with CONTINUE and BREAK statement
num = 1
while num <= 10:
    num += 1
    if num%2 == 0:
        print(num)
    elif num%2 == 1:
        continue
num = 1
while num <= 10:
    num += 1
    if num%2 == 0:
        print(num)
    elif num%2 == 1:
        break

# 5. FUNCTION: block of code and only runs when it is called
#              information (known as parameters or arguments) can be passed into a function
def add(num1, num2):
    return num1 + num2
print(add(4, 5))
    # use control flow within a function
list_of_number = [12, 16, 17, 24, 29, 30]
def even_or_odd(list): # arguments can be list
    even_list = []
    odd_list = []
    for i in list:
        if i%2 == 0:
            even_list.append(i)
        elif i%2 ==1:
            odd_list.append(i)
    print(even_list)
    print(odd_list)
even_or_odd(list_of_number) # if use print in the function then the function can be called without print

# 6. LAMBDA: an anonymous and one line function, can take any number of arguments but only have one expression
#            syntax is lambda arguments : expression
addition_answer = lambda a : a + 10 # a is the argument and a + 10 is the expression
print(addition_answer(5)) # a = 5
multiply_answer = lambda a, b : a * b
print(multiply_answer(4, 6)) # a = 4, b = 6
    # power of lamda is better shown when use as an anonymous function inside another function
def function(n):
    return lambda a : a * n # the argument(n) will be multiply by an unknown number(a)
double = function(2) # create a function that always double the number that is sent in
                     # double = lambda a : a * 2
print(double(10)) # -> lambda 10 : 10 * 2

# 7. OBJECT ORIENTED PROGRAMMING (OOP) : real life stimulation containing object and class
# object: represent real world objects with attributes (data) and methods (behaviours)
# class: blueprint creating the object (a way to define the attributes and methods)
class Dog: # creating a class, name of the class must start with capital
    def __init__(self, name, height, weight): # creating attributes of the object
        self.name = name
        self.height = height
        self.weight = weight
    def eat(self): # creating the behaviours of the objects as method (function within a class is called method)
        print("{} is eating".format(self.name))
    def walk(self): # self is referring to the object itself
        print("{} is walking".format(self.name))
    def sleep(self):
        print("{} is now asleep ZZzzZ".format(self.name))

max = Dog("Max", 70, 40) # creating an object, max, for the Dog class
charlie = Dog("Charlie", 50, 20) # max and charlie are instances of the class Dog and each has three attributes

# calling different methods for each of the instances
max.eat()
charlie.sleep()
max.walk()

# 8. 4 PILLARS OF OOP
# 8a. Abstraction: hiding irrelevent information only showing essential and neccessary features to the user
from shape import Shape # importing the Shape class, hiding the class code from the users
rectangle = Shape(2, 3)
print(rectangle.get_area())
# 8b. Inheritance: define a class (child class) that inherits all the methods
#                  and properties from another class (parent class)
# creating a database to store every person at Sparta, with employee and trainee
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print("{} {}".format(self.firstname, self.lastname))
class Employee(Person): # employee is the child class and person is the parent class
    def __init__(self, firstname, lastname, employee_id):
        super() .__init__(firstname, lastname) # inheriting from the person class, super() is needed
        self.employee_id = employee_id

    def print_employee_id(self):
        print("My name is {} {} and my employee id is {}.".format(self.firstname, self.lastname, self.employee_id))
trainer1 = Employee("Isabella", "Jones", 1001)
print(trainer1.print_name()) # inherit from the person class
print(trainer1.print_employee_id())
class Trainee(Person):
    def __init__(self, firstname, lastname, stream):
        super().__init__(firstname, lastname)  # inheriting from the person class, super() is needed
        self.stream = stream

    def trainee_course(self):
        print("{} {} is from the {} stream.".format(self.firstname, self.lastname, self.stream))
spartan1 = Trainee("Gigi", "Chiang", "Data 9")
spartan1.trainee_course()
# 8c. Encapsulation: restrict access to methods and attributes of a certain class
#                    prevents accidental modification of data and unwanted changes
#                    create private attributes and methods using __ in front of the attributes or methods
class Car:
    def __init__(self, model, passengers, colour, speed):
        self.model = model
        self.passengers = passengers
        self.colour = colour
        self.speed = speed

    def __display(self): # this method becomes private
        print("This is a {} {}".format(self.colour, self.model))

    def accelerate(self):
        self.speed = self.speed + 2
        print(self.speed)

ferrari = Car("Ferrari", 2, "black", 10)
ferrari.accelerate()
ferrari.display() # not accessible from the object (attributeerror: 'Car' object has no attribute 'display')
# 8d. Polymorphism: the ability to take different forms
#      - Method Overriding: in inheritance, allows user to define methods in the child class with
#                          same name as in the parent class -> gives different output
class Animal:
    def eat(self):
        print("{} is easting slowly".format(self.__class__.__name__))
class Dog(Animal): # inheriting the animal class
    def eat(self): # overriding the eat method with a new output
        print("Dog is eating super fast")
class Cat(Animal):
    pass
karlo = Dog()
lumi = Cat()
for animal in (karlo, lumi):
    animal.eat() # karlo is running the eat method in dog class while lumi is running the eat method in animal class
#      - Method Overloading: same function with different parameters
class Area:
    def get_area(self, width, height = None):
        if height is not None:
            return width * height
        else:
            return width * width
square = Area()
rectangle = Area()
print("Area of the square is", square.get_area(4)) # calling the method with 1 parameter
print("Area of the rectangle is", rectangle.get_area(4, 5)) # calling the method with 2 parameters
