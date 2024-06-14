# s = 1+4+7+10+13+16+19
# s = 0
# for x in range(1,20,3):
#     s = s+x
# print("Soma =", s)

# nome = input("Qual e o seu nome: ")
# print("Bom dia",nome)

# idade = int(input("Qual e a sua idade: "))
# print(idade)
# print(type(idade))

# a = "Python"
# count_n = a.count("n")
# print(count_n) 
# print(a.count("n"))

# a = "Jess"
# size= len(a)
# print(size)
# print(len(a))

# #String manipulation, you can assign the result to a variable and then print the variable, or you can call the function inside of print().

#Storing result in a variable and then priting the variable
# a = "Jess"
# ends_with = a.endswith("ss")
# print(ends_with)

# Calling the fuction inside of print()
# a = "Jess"
# print(a.endswith("ss"))

# a = "Jess"
# starts_with = a.startswith("Je")
# print(starts_with)

# a = "Jess"
# upper_case = a.upper()
# print(upper_case)

# a = "Jess"
# print(a.upper())


# #Acessing characters in strings 

# a = "Jessica"
# print(a[:2])
# print(a[0])

# a = "Um elefante incomanda muita gente"
# print(a[2:21])

# a = input("Write down a frase: ")
# print(a.upper(), a.lower())

#calculadora Z
# def calculate_z(x,y):
#     z = x + y
#     return z

# Get input from the user
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# Calculate z using the function
# z = calculate_z(x, y)

# # Print the result
# print("The value of Z is:",z)


# Definition + name of fuction + parameters,if none leave it blank() :
# def adjust_salary():
# # Identetion first, variable = value, in this case salary plus 35% increase
#     adjusted_salary = salary * 1.35
# # returns + variable  
#     return adjusted_salary

# # Get input from user
# salary = float(input("Enter your salary: "))

# #Calculates new salary using variable = function
# adjusted_salary = adjust_salary()

# # Print the adjusted salary
# print("Your new salary after 35% increase is", adjusted_salary)

#LISTS

# list = ["apple", "kiwi", "orange"]
# list.reverse()
# list.append("strawberry")
# print(list)

# L = [1,2]
# R = [L * 4]
# print(R)

# J = ["Apple", 2, 3, "Berries"]
# print(J[:2])
# print(J[1])

# L1 = list(range(1,50,3))
# print(L1)

# L2 = [5,7,2,9,4,1,3]

# print(len(L2),max(L2),min(L2),sum(L2),sorted(L2))

# def calculate_rocket_fuel_required(distance):
#     fuel = distance * 15
#     if fuel < 100:
#         return 100
#     else:
#         return fuel
# print(calculate_rocket_fuel_required(20))

# nota_media = {"Jess":7, "Joao":5, "Luke":10}

# print(nota_media)

# nota_media["Jess"] = 5
# print(nota_media)

# nota_requerida = 7

# if nota_requerida in nota_media.values():
#     print(f"Yes there's a {nota_requerida}")

# else:
#     print(f"There's no {nota_requerida}")

# STR.format

# name = "Jess"
# age = 33

# # print("{} is {} years old".format(name,age))

# name_age = "{} is {} years old".format(name,age)
# print(name_age)

# nota_media = {"Jess":7, "Joao":5, "Luke":10}

# import statistics
# numbers = [8,7,10]
# median = statistics.median(numbers)
# print(f"The median is: {median}")

#Python library

# icecream = input("What's your favourite ice cream flavour? ").lower()

# if icecream == "chocolate":
#     print("You have good taste!!")
# elif icecream == "vanilla":
#     print("That's weird!!")
# elif icecream == "strawberry":
#     print("You must be a kid") 
# else:
#     print("Ok, which one is it then?")       

# idade = int(input("Qual a sua idade? "))

# if idade > 60:
#     print("You are in the best age!!")
# elif idade > 10 and idade < 30:
#     print("You have a lot to learn!!")
# else:
#     print("Enjoy it, because time flies!!")    

#Program school marks

# #Importing statistics functions to later use median()
# import statistics

# # #Assigning mark 1, mark 2
# mark1 = 4
# mark2 = 7

# #Creating a list of marks
# marks = [mark1, mark2]

# #Calculating the median
# median = statistics.median(marks)

# #Printing the median mark
# print(f"The median mark is: ",median)

# #Checking if the median is sufficient to pass
# if median >= 6:
#     print("Congratulations, you have passed!!")
# elif median > 4 and median < 6:
#     print("You did ok, better to study more next time")   
# else:
#     print("You haven't passed, you need to study more!")

#LOOPS

# password = "12345"
# input_user = ""
# while input_user != password:
#     input_user = input("Digite your code: ")
#     if input_user == password:
#         print("Access granted")
        
#     else:
#         print("Try again")

# Find the sum of S = 1+4+7+10+13+16+19

# S = 0
# for x in range(1,20,3):
#     S = S+x
# print("Sum = ",S)        

# Calculate median for students marks

# Marks_list = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
# sum = 0

# for nota in Marks_list:
#     sum = sum + nota
# marks_mean = sum/len(Marks_list)
# print("Median =", marks_mean)

# Function, how to define a .function

# def hello_function():
#     print("Helllo world!!")

# hello_function()

# Parameters and arguments
# Function to print higher number between two numbers, remember to see the result you can call the function.

def higher_number (x,y):
    if x > y:
        print(x)
    else:
        print(y)    

higher_number(9,7)      

