# A
x = 5
y = 6
if x > y:
    print("BIG")
else:
    print("small")

# B
for i in range(5):
    print(i)

# C
season = 1
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("Error!!!")

# D
count = 1
while count < 11:
    print(count)
    count += 1

# E
age = 27
first_letter_of_last_name = "s"
shekel_dollar = 3.26
did_you_fly_abroad = True
your_apartment_number = "36"

print(age, first_letter_of_last_name, shekel_dollar, did_you_fly_abroad, your_apartment_number)
print(age + shekel_dollar)

# F
phone_number = input(str("Enter you phone-number: "))
print(f"phone number {phone_number}")

# G
def print_hello():
    print("Hello")


def calculate(num1, num2):
    result = num1 + num2
    print(result)


user_input1 = input(str("please enter the first number: "))
user_input2 = input(str("please enter the second number: "))

calculate(user_input1, user_input2)


# H
def print_name(name):
    print(name)


def divide_by_two(num):
    result = num / 2
    print(result)


user_input3 = input(str("What's your name: "))
print_name(user_input3)

user_input4 = input("Enter a number: ")
x = int(user_input4)
divide_by_two(x)

# I

def add_two_numbers(number1, number2):
    return number1 + number2


def add_space(str1, str2):
    return str1 + " " + str2






