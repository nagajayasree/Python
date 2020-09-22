# # Variables
print("Hello World")
age = 28
print(age)

# # Receiving Input
# name = input("What is your name? ")
# print("Hello " + name)

# type conversion
birth_year = input("Birth year: ")
age = 2020 - int(birth_year)
print(age)

# # Strings exercise
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

course = 'Python for Beginners'
print(course.upper())
print(course.replace('for','4'))
print(course)
print('Python' in course)

# # ArithmeticOp
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 % 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)

# # Operator Precedence
print(10 + 3 * 2)
print((10 + 3) * 2)

# # Comparison
x = 3 > 2
print(x)


# Logical op
price = 10
print(price > 12 and price == 10)
print(price > 12 or price == 10)
print(not price > 12)

# if stmt
temp = 30
if temp > 30:
    print("It's a hot day")
    print("Turn on AC")
elif temp > 20:
    print("It's a nice day")
elif temp > 10:
    print("It's bit cold")
else:
    print("It's cold")
print("Done")

# Exercise
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


# While loop
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

# Lists
names = ["Vimmy", "Jay", "Sai"]
names[1] = "Jaya"
print(names)
print(names[0:2])

# List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0,-1)
numbers.remove(5)
# numbers.clear()
print(numbers)
print(1 in numbers)
print(len(numbers))

# for loop
for item in numbers:
    print(item)

# range function
numbers = range(5,10,2)
for number in numbers :
    print(number)

# tuples
nums = (1, 2, 3, 3)
nums.count(3)
nums.index(3)
