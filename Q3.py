import sys

array = []

array = input("please enter 5 numbers to take highest and least number ? ").split(" ")

if not len(array) == 5 :
    sys.exit("len of array is not 5 ")


integer_array = []

for item in array:
    integer_array.append(float(item))

integer_array.sort()

# len(integer_array)-1

print("max number is ",integer_array[4])

print("min number is ",integer_array[0])