import fibo                     # import the entire file
fibo.fib(100)

from fibo import fib            # import a specific function from the file
fib(100)

from fibo import fib as my_fib  # import a specific function from the file and locally rename it
my_fib(100)