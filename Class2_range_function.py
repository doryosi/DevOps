my_str = "Hello World"
primes = ["a", "b", "c", "d", "e"]

for p in range(len(primes)):  # run 5 times because the list length is 5 and print the index of each element in the list
    print(p)

print("########################################")

for p in range(len(primes)):  # run 5 times because the list length is 5 and print the element in the list
    print(primes[p])

print("########################################")

for p in range(len(primes)):  # run 5 times because the list length is 5 and print the element and its index
    print(p, primes[p])
