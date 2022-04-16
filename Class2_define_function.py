def get_numeric(number):
    numbers = ["zero", "one", "two", "three", "four"]
    if number < len(numbers):
        return numbers[number]
    else:
        return "not supported"


input_from_user = int(input("enter number: "))
print(get_numeric(input_from_user))

