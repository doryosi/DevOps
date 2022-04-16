def div_numbers(num1, num2):
    result = int(num1 / num2)
    print(result)


try:
    div_numbers(8, 2)
    div_numbers(8, 0)
except ZeroDivisionError as e:  # to exclusively catch a Zero Division Error
    print("Could not divide by zero")
except BaseException as e:  # to find out and catch the particular error
    print(e.args)           # print the particular error
    print("something went terribly wrong")

print("Script ended successfully")
