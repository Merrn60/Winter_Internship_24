def count_specific_digit(n, d):
    count=0
    for i in n:
        if i== d:
            count+=1
    print("The count of number appear ",count ,"times")






















input_N = input("Enter a number: ")
input_D = input("Enter a number: ")
count_specific_digit(input_N,input_D)
