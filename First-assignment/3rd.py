def sum_of_digits_consecutive_powers(n):
    count=0
    for i in n:
        count+=int(i)**int(i)
    print(count)








input_num = input("Enter a number: ")
sum_of_digits_consecutive_powers(input_num)