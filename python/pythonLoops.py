# Task 1 - for loop
# print all even numbers from 1-20
for i in range(1, 20):
    if i%2 == 0:
        print (i)
        i=i+1

# Task 2 - while loop
# ask user for number until they enter 0.
sum = 0
while True:
    number = int(input("Enter number here: "))
    if number != 0:
        sum = sum + number
    else:
        print (f"The updated sum of all previous entries is: {sum}")
        break

# Task 3 - for loop
# print multiplication table of 5
for i in range (1,11):
    print (i * 5)
    i+1

# Task 4
# calculate how many times a character gets repeated in a word
dictionary = {}
text = "phenomenon"
for letter in text:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1
print (dictionary)

# Task 5
# To do menu
to_do_list = []
while True:
    print ("------To do Menu--------\n")
    
    print("Input 1 for adding to do task")
    print("Input 2 for showing to do task")
    print ("Input 3 for Exit\n")

    choice = input("Enter your choice here (1/2/3): ")
    if choice == "1":
        task = input("Enter your task here: ")
        to_do_list.append(task)
        print(f"A new task -> {task} <- has been added successfully")
    elif choice == "2":
        if not to_do_list:
            print("List is empty. No entries made yet")
        else:
            for index, entry in enumerate(to_do_list, start=1):
                print(f"{index}. {entry}")
    elif choice == "3":
        print("Exiting system")
        break
    else:
        print("unsupported type of entry. Please select from 1,2 or 3.")

# Task 7
# create banking system using functions
accounts = {
    "jon": 100,
    "snow": 200,
    "arya": 300,
    "stark": 400
}

def check_balance(person):
    if person in accounts:
        print("we have an account with you. Please proceed")
        print(f"your balance is {accounts[person]}")
    else:
        print("we dont seem to have any account with you.")

def deposit(person):
    if person in accounts:
        amount = float(input("Enter how much money would you like to deposit: "))
        accounts[person] = accounts[person] + amount
        print(f"your updated balance is {accounts[person]}")
    else:
        print("user not found")

def withdraw(person):
    if person in accounts:
        amount = float(input("Enter how much money would you like to withdraw: "))
        if amount > accounts[person]:
            print("you dont seem to have enough money in the account for this withdrawl")
        else:
            accounts[person] = accounts[person] - amount
            print(f"your updated balance is {accounts[person]}")
    else:
        print("user not found")


while True:
    print("welcome to Raman Bank. We make you rich $$$\n")

    print("press 1 for dispositing money")
    print("press 2 for withdrawing money")
    print("press 3 for checking balance")
    print("press 4 for exit\n")

    print("please tell me who you are first\n")
    person = input("Enter your name here: \n")
    choice = input("Please provide your choice (1/2/3/4): \n")

    if choice == "1":
        deposit(person)

    elif choice == "2":
        withdraw(person)

    elif choice == "3":
        check_balance(person)
    elif choice == "4":
        print ("Exiting terminal")
        break
    else:
        print("not a valid choice provided. please provide 1/2/3 or 4")
