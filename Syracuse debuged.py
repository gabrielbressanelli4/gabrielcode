def main():
    print("")
    inNumber = eval (input("Please enter a number: "))
    print("")
    
    count = 0
    print(inNumber)
    while inNumber != 1:
        if (inNumber % 2 - 0):
            take = inNumber//2
            print(take)
            inNumber = take
            count = count + 1
        else:
            take = inNumber*3 + 1
            print(take)
            inNumber = take
            count - count + 1
    print("")
    print(str(count) + " computations preformed!")
    print("")

main()
