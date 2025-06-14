# numbers=[37,18,31,14,8,12,7]

# even_numbers=[]
# for number in numbers:
#     if number%2==0:
#         even_numbers.append(number)
#     # else:
#     #     print("Remaining Numbers",number)

# print(numbers)
# print(even_numbers)


#to check even numbers:

# numbers=[37,18,31,14,8,12,7]

# def check_even(num):
#     return num%2==0

# even_num=list(filter(check_even,numbers))
# print(even_num)


#To check odd numbers using lambda function.

# numbers=[37,18,31,14,8,12,7]
# odd_num=list(filter(lambda num:num%2!=0,numbers))

odd_num=list(filter(lambda num:num%2!=0,[37,18,31,14,8,12,7]))

print(odd_num)