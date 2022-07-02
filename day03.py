#  01. local variables and global variables in Python

# a = 10

# def display():
#     global a
#     a=12
#     print(a)

# print(a)
# display()
# print(a)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 02. type conversion in Python

#Implicit Type Conversion
# a = 10
# b = 10.25

# print(f'a = {a} is {type(a)}')
# print(f'b = {b} is {type(b)}')

# c = a + b

# print(f'c = {c} is {type(c)}')


#Explicit type conversion
# string = '10010'
# print(f'variable string datatype is {type(string)}')

# new_int = int(string, 2)
# print(f'new_int is {new_int} and its datatype is now {type(new_int)}')

# new_float = float(string)
# print(f'new_float is {new_float} and its datatype is {type(new_float)}')


# ------------------------------------------------------------------------------------------------------------------------------------------


# 03. What is __init__

# class old_class:
#     def __init__(self):
#         print('Old class constructor ran...')
        
#     def add(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         num3 = self.num1 + self.num2
#         print(f'{self.num1} + {self.num2} = {num3}')

# # old_obj = old_class(2, 3)
# # old_obj.add()


# # inheritance using init

# class new_class(old_class):
#     def __init__(self):
#         print("New class constructor ran...")
#         super().__init__()

#     def display(self, name):
#         self.name = name
#         print("My name is " + name)

# new_obj = new_class()
# new_obj.add(2, 3)
# new_obj.display('Rishabh')


# ------------------------------------------------------------------------------------------------------------------------------------------


# 04. lambda function
 
# x = lambda a : a * 2
# print(x(2))



# def funct(n):
#     return lambda x : x * n

# y = funct(2)

# print(y(11))


# ------------------------------------------------------------------------------------------------------------------------------------------


# 05. self in Python

# class my_class:
#     def __init__(self):
#         pass

#     def name_display(self, name):
#         self.name = name
#         print('My name is ' + self.name)
    
# my_obj = my_class()
# my_obj.name_display('Anthony Gonsalves')


# ------------------------------------------------------------------------------------------------------------------------------------------


# 06. How does break, continue and pass work

# # Break
# for i in range(10):
#     if i < 5:
#         print(i)
#     else:
#         print('break! loop exited.')
#         break


# # Continue
# for i in range(10):
#     if i == 6:
#         print('Continue! No 6 will be printed here.')
#         continue
#     print(i)


# # Pass
# class my_class:
#     pass

# my_obj = my_class()


# ------------------------------------------------------------------------------------------------------------------------------------------


# 07. What does [::-1} do?

# string = '1R O T A S  2 O P E R A  3 T E N E T  4 A R E P O  5 S A T O R'

# print(string[::-1])


# ------------------------------------------------------------------------------------------------------------------------------------------


# 08. randomize the items of a list in place in Python

# import random

# char_list = ['A', 'B', 'C', 'D', 'E']
# new_char_list = []
# loop_runs = True

# while loop_runs:
#     char = char_list[random.randint(0, len(char_list)-1)]
#     if char not in new_char_list:
#         new_char_list.append(char)
    
#     if len(new_char_list) == len(char_list):
#         loop_runs=False
        

# print(new_char_list)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 09. python iterators iterables and generators

# string = 'ALEXA'

# next_char = iter(string)

# print(next(next_char))
# print(next(next_char))
# print(next(next_char))
# print(next(next_char))
# print(next(next_char))


# def my_gen():
#     n = 1
#     yield(n)
    
#     n += 1
#     yield(n)

#     n += 1
#     yield(n)

# for i in my_gen():
#     print(i)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 10. generate random numbers in Python

# import random
# print(f'Your lucky number is {random.randint(0, 100)} today.')


# ------------------------------------------------------------------------------------------------------------------------------------------


# 11. capitalize the first letter of string

# text = input("Enter a string : ")
# print(text.title())


# ------------------------------------------------------------------------------------------------------------------------------------------


# 12. purpose of is, not and in operator

# string_list = ['A', 'B', 'C', 'D', 'E']
# E = 'E'
# for char in string_list:
#     if char is E:
#         string_list.append('F')

#     elif 'F' not in string_list:
#         print(char)
#     else:
#         print(string_list)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 13. ternary operators = conditional expression is an operation evaluates sumthing based on condition

# x = 0

# for i in range(10):
#     x = x+1 if i<5 else x-1
#     print(x)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 14. What does this mean: ? And why would we use it?

# string = 'dfhhilewgrehfak'
# print(string[2:4])


# ------------------------------------------------------------------------------------------------------------------------------------------


# 15. What are negative indexes and why are they used?

# string = "aaaabbbbccccdddd"
# # print(string[-9:-1])
# # print(string[:-4])
# print(string[-5:])


# ------------------------------------------------------------------------------------------------------------------------------------------


# 16. How to import modules in python?

# from turtle import Turtle, exitonclick

# turtle = Turtle()

# exitonclick()


# ------------------------------------------------------------------------------------------------------------------------------------------


# 17. create an empty class in Python

# class EmptyClass:
#     pass

# my_obj = EmptyClass()
# print(my_obj)


# ------------------------------------------------------------------------------------------------------------------------------------------


# 18. difference between list and tuples

# name_tuple = ('Rishabh', 'Sachin', 'Dheeraj')

# try:
#     name_tuple.append('Shreya')
# except:
#     print('Tupple is immutable.')


# ------------------------------------------------------------------------------------------------------------------------------------------


# 19. Create a File name abc.txt and write something in it

# with open("abc.txt", mode='w') as file:
#                 file.write('Day 03 02-07-2022 Tasks completed at 19:23Hrs.')
