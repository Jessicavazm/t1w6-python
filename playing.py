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

# String manipulation, you can assign the result to a variable and then print the variable, or you can call the function inside of print().

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

L2 = [5,7,2,9,4,1,3]

print(len(L2),max(L2),min(L2),sum(L2),sorted(L2))