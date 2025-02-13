# 1
def my_function (a,b):
    print(a,b)

my_function( 10 ,6 )
# 2
def fizz_buzz (nums):
    if  nums % 3 == 0 and nums % 5 == 0:
        print ("FizzBuzz")
    elif nums % 5 == 0:
        print ("Buzz")
    elif nums % 3 == 0:
        print("Fizz")
    else :
        print(nums)

fizz_buzz(34)
# 3
def check_speed(speed):
 
    speed_limit = 70
    
    
    if speed < speed_limit:
        print("Ok")
    else:
       
        points = (speed - speed_limit) // 5
        
        if points > 12:
            print("License suspended")
        else:
            print(f"Points: {points}")
check_speed (90)
# 4
def show_numbers(limit):
    for i in range(limit + 1): 
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
show_numbers(6)
# 5
def limit_numbers(numbers):
    for i in range(numbers+1):
        if i % 3 == 0 or i % 5 ==0:
            print(i)
limit_numbers(20)
# 6
def show_stars(rows):
    for i in range(1, rows + 1):  
        print('*' * i)  
show_stars (5)
