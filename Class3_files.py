def append_name(name):
    with open("names.txt", "a") as handler:  # open a file and close it once the scope ends
        handler.write(name + "\n")


def bless_names():
    file = None
    try:
        file = open("names.txt")
        file.seek(0)                      # move the cursor to the 0 position, i.e. the beginning of the file
        for file in file.readlines():
            print(f"Hey {file}", end="")  # the end is needed so the lines don't have a line gap between them
    except FileNotFoundError as e:
        print("unable to find file: " + str(e.args))
        if "file" in vars():  # a builtin function that returns a list of all variables within the local scope
            file.close()


for i in range(3):
    user_input = input("Enter you name: ")
    append_name(user_input)
bless_names()
