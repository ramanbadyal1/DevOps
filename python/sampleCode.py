name = "Raman"

# fstring
print (f"my name is {name}")

#input variables
name = input("what is your name? ")
print (f"your name is {name.upper()}")

#arithmatic operations
x = 10
y = 20
print (f"the sum of both is {x+y} subtraction is  {x-y}")

# if loops
age = 20
is_citizen = True

if age >=18 and is_citizen:
    print (f"you are eligible to vote")
else:
    print (f"you are not eligible to vote")

#task1
name="raman"
password="password"

new_name = input("Please enter your name: ")
new_password = input("Please enter your password: ")

if new_name==name and new_password==password:
    print(f"your entries are not successful")
else:
    print(f"your entries were successful")

#task2
number = int(input("Please enter your number: "))

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

if sign == "zero":
    print("The number is zero (and even).")
else:
    print(f"The number is {sign} and {parity}.")

#lists
fruits = ['apple', 'orange', 'kiwi']
print(fruits)

people = [
    ['Tom', 5],
    ['Dick', 10],
    ['Harry', 15]
]
print(people[0][0])

# add to list
fruits = ['apple', 'orange']
print (fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove("kiwi")
print(fruits)

# dictionary
my_data = {
    'name': 'Raman',
    'country': 'Canada',
    'age': 35,
    'is_citizen': True
}
print (my_data['is_citizen'])

print (my_data.keys())
print (my_data.values())
