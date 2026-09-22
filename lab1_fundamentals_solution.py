"""
Lab 1 - Fundamentals of Python: Errors, Variables and Expressions
(100 marks in total, including 5 exercises)

Your Name 😍:
Lab Due: 5:00pm on Sept. 17, 2026

Objective (By the end of this lab, you will be able to):
1. understand what a comment is in Python
2. recognize common errors in coding: syntax error, semantic (logic) error, and runtime error
3. debug simple Python programs by fixing common errors
4. Practice how to use variables, expressions and statements in Python
5. Practice working with different data types: int, float, str
6. Practice how to use operators and built-in functions such as print() in Python
"""

#-------What is a comment in programming languages?---------------------------------
# A regular comment in Python usually starts with a #. 
# Regular comments are used to explain parts of the code for developers reading it.
# Comments are not run as code by the interpreter.
# So this part is a comment. # is only able to comment one line at a time. 
# If you want to comment multiple lines, 
# you can use command + / (Mac) or ctl + / (Windows). 
# Or you can use ''' ''' or """ """ to create a multiline string or a docstring. 
#---------------------------------------------------------


#---------------------------------------------------------
# Exercise 1 (10 marks) 
# When you run the code in line 34, you can see the output "Hello, World!".
# Modify that line of code so that it prints "Hello, COMP115!" instead.
#---------------------------------------------------------

print("Hello, COMP115!")





#---------------------------------------------------------
# Exercise 2 (10 marks)- syntax error 
# Firstly, uncomment the line 46.
# Then fix its syntax error, to make it print the result of 5 + 6.
#---------------------------------------------------------

print(5 + 6)





#---------------------------------------------------------
# Exercise 3 (10 marks) - Semantic error
# Firstly, uncomment the line 58.
# Then fix its semantic error, to make it calculate the area of the rectangle correctly.
#---------------------------------------------------------

print("The area of a rectangle with length 3 and width 4 is", 3 * 4)





#---------------------------------------------------------
# Exercise 4 (10 marks) - Operator Precedence
# Add parentheses in line 70 so that new_num has the value 25
#---------------------------------------------------------

num = 5
new_num = num * (10 - 5)   # Add parentheses so that new_num has the value 25
print(f"Exercise 4: new_num stores the value of {new_num}.")





# ---------------------------------------------------------
# Exercise 5 (20 marks)
# Modify the operators in line 86 and 87 so that
# quotient and remainder store the correct results as hinted.
# ---------------------------------------------------------
dividend = 10
divisor = 3
division_result = dividend / divisor

quotient = dividend // divisor     # The quotient should be 3
remainder = dividend % divisor    # The remainder should be 1





# ---------------------------------------------------------
# Exercise 6 (40 marks)
# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.
# ---------------------------------------------------------

# Your code for the exercise 6 starts from here

current_time = int(input("Enter the current time:"))
time_to_wait = int(input("Enter the hours to wait:"))
alarm_time = (current_time + time_to_wait) % 24
print(f"The alarm time is {alarm_time}.")







#---------------------------------------------------------
# Submission (10 marks):
# After you finish this lab, copy all your code (Ctrl/Cmd + A)
# from this lab and paste it into the Lab1 assignment submission area on e-Learn.
# Good job. Congratulations on finishing your lab1!
#---------------------------------------------------------
