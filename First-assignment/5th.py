def multiply_digits(n):
    count=1
    for i in n:
         count*=int(i)
    print("The multiply digits ",count )






input_N = input("Enter a number: ")

multiply_digits(input_N)
