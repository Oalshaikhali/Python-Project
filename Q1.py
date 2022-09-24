5import time
import sys


print("Hello User")

time.sleep(3)

# name = input("please enter your Name ?")
# print("name")
#
# age = input("please enter your Age ?")
# print("age")
#
# address = input("please enter your Address ?")
# print("address")
#
# print(f"Hello Mr/Ms {name} age {age} located in {address}. thanks for being one of our community,    Enjoy")


# print("please enter your Name and age and address ?")
# name = input()
# age = input()
# address = input()
try:
    name , age, address = input("please enter your Name and age and address ?").split(" ")
except:
    sys.exit("one or more items are empty")

# print(type(name))
# if not isinstance(name, str):
#     print("the name is not string ")
#     exit()
#
# if not type(age) == "<class 'str'>":
#     print("the name is not string ")
#     exit()
# if not type(address) == "<class 'str'>":
#     print("the name is not string ")
#     exit()
error_flag = False
try:
    name = int(name)
    error_flag = True
except:
    name=name

if error_flag:
    sys.exit("the name is not string ")

error_flag = False
try:
    age = int(age)
except:
    error_flag = True

if error_flag:
    sys.exit("the age is not integer ")


print(f"Hello Mr/Ms {name} age {age} located in {address}. thanks for being one of our community,    Enjoy")