def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

num = 153
print(is_armstrong(num)) 

num = 9474
print(is_armstrong(num))  

num = 123
print(is_armstrong(num)) 
