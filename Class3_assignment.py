# 1
a = 1/0

# 2
try:
    a = 1/0
except ZeroDivisionError as error:
    print(error.args)

# 3
# The code is legal but unnecessary since there isn't any error handling
try:
    x = 1
finally:
    print("finally")

# 4
# What exception types can be caught by the following handler?
# Except:
# Nothing since it's not a reserved word since it begins with a capital "e"

# 5
# It's not a reserved word since the reserved word is "except"

# 6
# except IOError - any input/output errors such as: file doesn't exist, doesn't found, cannot be opened for writing/reading
# except ZeroDivisionError - when a number is divided by zero

# 7-9
with open("words.txt", "w+") as my_file:
    my_file.write("Dor\n")
    my_file.seek(0)
    print(my_file.read())

# 10
with open("words.txt", "w+") as my_file:
    my_file.write("שלום, קוראים לי דור\nזאת השורה השנייה\n")
    my_file.seek(0)
    print(my_file.readlines())
