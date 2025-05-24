def remove_digit(n, d):
    result=""
    for i in n:
        if i==d:
            continue
        result+=i



    print(result)













input_N = input("Enter a number N: ")
input_D = input("Enter a number D: ")
remove_digit(input_N, input_D)
