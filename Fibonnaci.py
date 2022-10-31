# This program computes and outputs the nth Fibonacci number
# with a value entered by the user.

number = eval(input("Insert a positive value: "))

prev = 1
fib = 1
for i in range (2,number):
    temp = prev
    prev = fib
    fib = temp + fib

print("The value of Fibonacci(" + str(number) + ") is", fib)
