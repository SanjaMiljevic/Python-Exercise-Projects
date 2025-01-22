# This is a FizzBuzz program that prints numbers from 1 to 50.
# For multiples of 3, it prints "Fizz", for multiples of 5, it prints "Buzz".
# For numbers that are multiples of both 3 and 5, it prints "FizzBuzz".
# For all other numbers, it simply prints the number itself.


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
