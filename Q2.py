import sys
import math

# while_flag = True
# while while_flag:
#     try:
#         num1 , num2 = input("enter two number ").split(" ")
#         while_flag = False
#     except:
#         print("Invalid input, Please try again! ")


while True:
    try:
        num1 , num2 = input("enter two number ").split(" ")
        error_flag1 = False
        try:
            num1 = float(num1)
        except:
            error_flag1 = True

        if error_flag1:
            print("the num1 is not number ")


        error_flag2 = False
        try:
            num2 = float(num2)
        except:
            error_flag2 = True

        if error_flag2:
            print("the num2 is not number ")

        if not error_flag1 and not error_flag2:
            break

    except:
        print("Invalid input, Please try again! ")



# print("please choose one of the symbols and enter it's number")
# print("1 or +")
# print("2 or -")
# print("3 or *")
# print("4 or /")
# print("5 or ^")
# print("6 or %")

second_operation_str = "please choose one of the symbols and enter it's number \n 1 or + \n 2 or - \n 3 or * \n 4 or / \n 5 or ^ \n 6 or %"


result = 0
while True:
    print(second_operation_str)
    try:
        operation = input()


        if operation == "1" or operation == '+':
            result = num1 + num2

        elif operation == "2" or operation == '-':
            result = num1 - num2

        elif operation == "3" or operation == '*':
            result = num1 * num2

        elif operation == "4" or operation == '/':
            result = num1 / num2

        elif operation == "5" or operation == '/':
            result = num1 ^ num2

        elif operation == "6" or operation == '%':
            result = num1 % num2
        else:
            print("Invalid input, Please try again! ")

        if not result == 0:
            break

    except:
        print("Invalid input, Please try again! ")

print(f"the result is {result}")



while True:
    try:
        print("Please choose your options ")
        print("1- Approx ceil, floor, trunc")
        print("2- Result  as integer")
        print("3- Exit")


        seconed_operation= input("please enter number of choice ")

        if seconed_operation == "1" :

            print(" 1- approx ceil ", math.ceil(result))
            print(" 2- approx floor ", math.floor(result))
            print(" 3- approx trunc ", math.trunc(result))


        elif seconed_operation == "2" :
            print("Result as integer",int(result))

        elif seconed_operation == "3" :
            print("Program Ended")
            # sys.exit("program ended")


        if  seconed_operation == "1" or   seconed_operation == "2" or seconed_operation == "3":
            break


    except:
        print("Invalid input, Please try again! ")
