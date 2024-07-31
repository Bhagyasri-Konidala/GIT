PROGRAM1:

#Display numbers from a list using loop
#if the number is greater than 500, then stop the loop
#if the number is greater than 150, then skip the loop
# the number must be divisible by 5

numbers = [12,75,155,180,145,525,50]
for item in numbers:

    if item > 500:#if the number is greater than 500, then stop the loop
        break
    elif item >150:#if the number is greater than 150, then skip the loop
        continue
    elif item % 5 == 0:# the number must be divisible by 5
        print(item)


PROGRAM2:

#count the total number of digits in a number
num = 456789321
count = 0
while num != 0:
    num = num//10
    count = count + 1
print("number of digits:" , count)

#SECOND METHOD
a = int(input("enter the numbers:"))
print('total number of digits: ', len(str(a)))


PROGRAM3:

#Define a function called multiply that takes two arguments and return their product
def multiply(x,y):
    result = x*y
    return result
result = multiply(6, 7)
print(result)


NOTE:return stmt purpose is to return the value at the same time terminates the function.


PROGRAM 4:

#accept the list of 5 float numbers
numbers = []
for i in range(0, 5):
    print("enter number:", i)
    item = float(input())
    numbers.append(item)
print("user list", numbers)

#SECONd METHOD:

numbers = [float(input("enter numbers: ")) for i in range (5)]
print("user list", numbers)



PROGRAM 5:

#print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

row = 5
for i in range(row):
    for j in range(i+1):
        print(j+1, end=" ")
    print()



PROGRAM 6

#calculate  the sum of all numbers from 1 to the given number

s = 0
n = int(input("enter value"))
for i in range(1, n+1, 1):
    s += i
print("\n") 

#SECOND METHOD

n = int(input("enter the number: "))
x = sum(range(1, n+1))
print("sum is", x)


PROGRAM 7

#check  if the first and last number of a list is the same

def first(numbers):
    print("given list:", numbers)
    first_num = numbers[0]
    last_num = numbers[-1]

    if first_num == last_num:
        return True
    else:
        return False


SECOND METHOD

x = [1,2,3,6,1]
print("result is", first(x))
y = [5,6,7,8,9]
print("result is", first(y))


PROGRAM 8

#print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for  i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



PROGRAM 9

#print the following pattern
# *
# * *
# * * *
# * * * *
# *
#print the following pattern
# *
# * *
# * * *
# * * * *
# * * * *  *


for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()


PROGRAM 10

#print the following pattern
#       1
#      1  2
#     1  2  3
#    1  2  3  4
#   1  2  3  4   5

n = 5
for i in range (1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end= " ")
    print()



PROGRAM 11

#write a program to display all prime numbers  within a range

start = 1
end = 50
print("prime numbers between ", start, "and", end, "are:")
for num in range(start, end+1):
    if num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)


PROGRAM 12

#calculate the cube of all numbers from 1 tona given number

n = 10
for i in range(1, n+1):
    print("current number is:", i, "and the cube is ", (i*i*i))


PROGRAM 13

#create a function  with variables length of arguments

def func1(*a):
    for i in a:
        print(i)

func1(1,2,3,4)
func1(5,6,7,8,9)


FOR STORING IN TUPLE
#createa function  with variables length of arguments FOR STORING TUPLE

def func1(*a):
    print(a)

func1(1,2,3,4)
func1(5,6,7,8,9)


PROGRAM 14

#return multiple values from a function

def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

res = calculation(40, 50)
print(res)


PROGRAM 15

#create a fun with a default argument

def employee(name, salary = 35000):               
    print("name:", name, "salary:", salary)

employee("viha", 26000)
employee("tanu", 28000)
employee("deepthi")
employee("jaya", 25000)


PROGRAM 16

#find the largest number from a given list using function

def largest_num(my_list):
    largest_num = max(my_list)
    return largest_num
my_list = [11,123,143,557,333,445,434]
result = largest_num(my_list)
print("the largest number is:", result)

PROGRAM 17

# display first letter of your name using function

def get_first_letter(string):
    words = string.split()
    first_letter = [word[0] for word in words]
    result_string = "" .join(first_letter)
    return result_string

input_1 = input("enter the name:")
print(f"the first letter of {input_1}", get_first_letter(input_1))





PROGRAM 18

#count the letters, digits and symbols from a given string

def find_digits(sample_str):
    char_count = 0
    digit_count = 0
    symbols_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbols_count += 1
    print("chars =", char_count, "digits =", digit_count, "symbols =", symbols_count)

sample_str = "vsmsd143@586#$%^"{sample_str = input("enter any :")}
find_digits(sample_str)





























































































































