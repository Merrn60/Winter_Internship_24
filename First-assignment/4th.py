def has_all_unique_digits(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]==n[j]:

                return False
    return True





input_num = input("Enter a number: ")
#has_all_unique_digits(input_num)
print("All unique digits found",has_all_unique_digits(input_num))