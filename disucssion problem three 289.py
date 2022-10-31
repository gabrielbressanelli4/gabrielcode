# Discussion Problem 3

# a)
value = 0
for num in range(n + 1):
    value += num


# c)
total = 0
user_num = eval(input('Enter a number, and put 999 if you want to stop:'))
while user_num != 999:
    total += user_num
    user_num = eval(input('Enter a number, 999 to quit: '))
