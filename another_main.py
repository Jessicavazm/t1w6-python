# Variables should have meaningfull names
num1 = 1
num2 = 1

num3 = 5
num3 = num3 + 2
print(num3)

num3+=3
print(num3)

total = num1 + num2 + num3
print(total)

# String interpolation
print("The total adition is",total)
print(f"The total addition is {total}")