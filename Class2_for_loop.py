for i in range(100):
    if i % 7 == 0:
        print(f"BOOM!!! {i}")
        continue                # keep running this block of code
    else:
        print(i)

for i in range(100):
    if i == 10:
        break                   # exit the loop

for i in range(100):
    if i == 5:
        pass                    # an empty block of code for later use
    else:
        print(i)
