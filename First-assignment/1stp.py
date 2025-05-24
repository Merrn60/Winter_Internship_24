def replace_digit_with_word(n):
    word=["zero","one","two","three","four","five","six","seven","eight","nine"]
    result=""
    for i in n:
        result+=word[int(i)]
    print(result)









input_num=input("Enter a number: ")
replace_digit_with_word(input_num)
