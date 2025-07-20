################# Print() #######
# print("Hello world again !!!!!")
# name = "Hridaya"
# host = "Notion"
# print("My name is :",name, " and i am attending workshop hosted by :",host)

# print("Cat","Dog","Bird",sep = " & ")

# print("🎉" * 10)

#-------------- input() ----------

# name = input("Enter your name :")
# print(f"Hello there, {name}")

# age = int(input("Enter your age :"))
# print(f"Ohhh, I see you'r {age} years old ,HUH")

# a,b,c=2,4,6
# print(a,b,c)

#---------Variables - Your Data Storage Units 📦-------------

# # Numbers
# pizza_slices = 8
# price = 12.99

# # Text (strings)
# favorite_movie = "The Matrix"
# emoji_mood = "😎"

# # Boolean (True/False)
# is_hungry = True
# loves_python = True  # Obviously!

# ageintext = "18"
# print(type(ageintext))

# print(ageintext+5) --- gives error

# age = int(ageintext)
# print(age + 5)

# # Float conversions
# price = float("19.99")
# whole_price = int(price)  # 19 (loses decimal)

# # Boolean conversions
# print(bool(0))      # False
# print(bool(42))     # True
# print(bool(""))     # False
# print(bool("Hi"))   # True

# print(bool(-1))

#---Exercise 1 ---

# age = int(input("Enter your age :"))
# o = age+10
# print(o)

#------------Conditional Statements - The Decision Makers 🤔---------------

# temperature = 25

# if temperature > 30:
#     print("🔥 It's hot! Time for ice cream!")
# elif temperature > 20:
#     print("🌤️ Perfect weather!")
# elif temperature > 10:
#     print("🧥 Grab a jacket!")
# else:
#     print("🥶 Brrr! Stay inside!")

# temperature = 25
# mood = "happy" if temperature > 20 else "grumpy"
# print(mood)

#-----------6. Comparison Operators - The Judges ⚖️---------

# # The usual suspects
# print(5 == 5)    # True (equal)
# print(5 != 3)    # True (not equal)
# print(5 > 3)     # True (greater)
# print(5 < 3)     # False (less)
# print(5 >= 5)    # True (greater or equal)
# print(5 <= 4)    # False (less or equal)

# # String comparisons
# print("apple" == "apple")  # True
# print("Apple" == "apple")  # False (case sensitive!)

# user_age = 18
# can_vote = user_age >= 18
# print(f"Can vote:", can_vote)

#--------- Logical Operators - The Connectors 🔗-------

# age = 25
# has_license = True
# has_car = False

# # AND - both must be true
# can_drive = age >= 16 and has_license
# print(f"Can drive: {can_drive}")

# # OR - at least one must be true
# can_travel = has_car or has_license
# print(f"Can travel: {can_travel}")

# # NOT - flip the boolean
# is_minor = not (age >= 18)
# print(f"Is minor: {is_minor}")

# can_uber = (age >= 18) and (not has_car) and has_license

# print(can_uber)

# age = int(input("Enter your age : "))

# if(age>0 and age<=16):
#     print("minor")
# elif(age>=17 and age<=70):
#     print("adult")
# else:
#     print("Senior") 


#------------8. For Loops - The Repetition Masters 🔄------------

# # Basic counting
# for i in range(5):
#     print(f"Count: {i}")

# # Counting with style
# for i in range(1, 6):
#     print("🎯" * i)

# # Looping through lists
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I love {fruit}!")

# # Looping through strings
# for letter in "PYTHON":
#     print(f"Letter: {letter}")

# netaharu = ["kp", "sheru", "puspa"]
# for index, neta in enumerate(netaharu):
#     print(f"{index}: {neta}")

#---------While Loops - The Persistent Ones 🔁--------

# # Basic while loop
# countdown = 5
# while countdown > 0:
#     print(f"Countdown: {countdown}")
#     countdown -= 1    # countdown = countdown - 1
# print("🚀 Blast off!")

# # User input loop
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
#     if password != "secret":
#         print("❌ Wrong password!")
# print("✅ Access granted!")

#----Exercise -3 ----------

# r = int(input("Enter Range :"))

# for i in range (0,r):
#     if(i%2==0):
#         print("Even")
#     else:
#         print("Odd")

#------Functions - Your Code Helpers 🛠️---------

# # Basic function
# def greet():
#     print("Hello, World!")

# greet()

# # Function with parameters
# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Alice")

# # Function with return value
# def add_numbers(a, b):
#     result = a + b
#     return result

# sum_result = add_numbers(5, 3)
# print(f"Sum: {sum_result}")

#--------Lists - The Ordered Collections 📝---------

# # Creating lists
# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, True, 3.14]

# # Accessing elements
# print(fruits[0])     # apple (first item)
# print(fruits[-1])    # cherry (last item)

# # Slicing
# some_fruits = fruits[1:3]
# print(some_fruits)

# # Useful methods
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


# scores = [85, 92, 78, 96, 88]
# scores.sort()           
# print(scores)           

# scores.reverse()
# print(scores)  

#-------- Dictionaries - The Key-Value Store 🗂️---------

# # Creating dictionaries
# student = {
#     "name": "Ram",
#     "age": 20,
#     "grade": "A",
#     "subjects": ["Programming", "Engineering"]
# }

# # Accessing values
# print(student["name"])
# print(student.get("age"))

# student["email"] = "ramu@example.com"
# student["age"] = 21
# print(student)

# li = [33,42,420,69,7]

# for i in range(0,len(li)):
#     if (li[i] % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

#------ Writing Reusable Scripts - The Philosophy 🎯--------

# Messy script - does everything at once
# print("Calculator")
# num1 = float(input("First number: "))
# num2 = float(input("Second number: "))
# result = num1 + num2
# print(f"Result: {result}")


#---------CALCULATOR--------

# print("Mini-Calculator")

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# a = int(input("Enter 1st number :"))
# b = int(input("Enter 2nd number :"))

# opt= int(input("""
# Enter 1 to add 
# Enter 2 to subtract
# Enter 3 to multiply
# Enter 4 to divide :
# """))

# if(opt == 1):
#     print(add(a,b))
# elif(opt == 2):
#     print(sub(a,b))
# elif(opt == 3):
#     print(multiply(a,b))
# elif(opt == 4):
#     print(divide(a,b))
# else:
#     print("Please input value 1 - 4")

#--------- Python Classes - Creating Your Own Objects 🏗️---------

# # Creating a simple class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I'm {self.age} years old!"


# # Creating objects (instances) from the class
# p1 = Person("KP Oli", 72)
# p2 = Person("Prachanda", 70)

# # Using methods
# print(p1.greet())
# print(p2.greet())

# # Accessing attributes
# print(f"{p1.name} is {p1.age} years old") # Bad Practice, but works

# # Use Getters and Setters for better practice
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def set_name(self, name):
#         self.name = name

#     def set_age(self, age):
#         self.age = age

# # Using class methods
# p1 = Person("Ramu", 25)
# print(p1.get_name())
# print(p1.get_age())


#---------Error Handling - Expect the Unexpected 🛡️-------

# #Divide by zero error
# a = 10
# try: 
#     result = a / 0
# except Exception as e:
#     print(f"Error: {e}")

# #Name Error
# try:
#     print(naam_xyna)
# except Exception as e:
#     print(f"Error: {e}")


# # Single Exception
# def safe_divide(a, b):
#     """Division that won't crash your program"""
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#         return None
#     except TypeError:
#         print("Please provide numbers!")
#         return None

# result = safe_divide(2, 0)

