def digit_difference(n):
    max=n[0]
    min=n[0]
    for i in n:
        if i>max:
            max=i

        if i<min:
            min=i


    diff=int(max)-int(min)
    print(diff)













input_D = input("Enter a number D: ")

digit_difference(input_D)
