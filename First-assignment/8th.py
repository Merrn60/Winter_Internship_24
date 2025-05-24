def swap_first_last_digit(n):
    first = n[0]
    last = n[len(n) - 1]

    result = last+n[1:len(n)-1]+first

    print(result)












input_D = input("Enter a number D: ")

swap_first_last_digit(input_D)
