def contains_digit(n, d):
    count=0
    for i in n:
        if i== d:
            count+=1



    if count>=1:
        return True
    else:
        return False






















input_N = input("Enter a number N: ")
input_D = input("Enter a number D: ")
print(contains_digit(input_N,input_D))
