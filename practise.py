# age = 4
# print(age)
# print("helloo","I am Himani","A Btech student","learning python currently")
# x=10
# print(type(x))
# x="Hello World"
# print(type(x))
# x=10.2
# print(type(x))
# x=True
# print(type(x))
# x=b"Hello"
# print(type(x))
# x=1j
# print(type(x))
# x={"name","age"} 
# print(type(x))
# x=("apple","banana","mango")
# print(type(x))
# x=["pen","pencil","book"]
# print(type(x))
# print(x == 1)
# print(x == 2)
# print(x != 1)
# print(x != 2)
# x=4
# print(x<5 and x<9)
# print(x>1 or x<5)
# print(not(x<5 and x<9))

# x=["maruti","BMW"]
# y=["maruti","BMW"]
# z=x
# print(z is x)
# print(x is y)
# print(x is not y)
# x=["himani","kuhu"]
# y="himani"
# print(y in x)
# name = input("please enter your name:")
# print("hello" ,name)

# x = input("Enter the first value for sum:")
# y = input("Enter the second value for sum:")
# z = x+y
# print("sum:",z)
# z = int(x)+int(y)
# print("sum:",z)

# x= input("Enter the value of first side:" )
# y= input("Enter the value of second side:")
# z =int(x ** 2)+int(y ** 2) ** 0.5
# print("sum:",z)


# print("+-----------+")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("+-----------+")




# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5, end="")
# print("+"+"-"*10+"+")

# number1 = int(input("enter the first number:"))
# number2 = int(input("enter the second number:"))
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# print("the largest number is:",larger_number)

# number1 = int(input("enter the first value:"))
# number2 = int(input("enter the second value:"))
# number3 = int(input("enter the third value:"))
# larger_number = number1
# if number2 > largest_number:
#     largest_number = number2
# if number3 > largest_number:
#     largest_number = number3
# print("the largest number is:",largest_number)


# number1 = int(input("enter the first value:"))
# number2 = int(input("enter the second value:"))
# number3 = int(input("enter the third value:"))
# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)
# print("the largest number is:", largest_number)
# print("the lowest number is:", lowest_number)


# while True:
#  print("I am a student") 

# largest_number = -999999999
# number = int(input("enter a number or type -1 to stop:"))
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("enter a number or type -1 to stop:"))
# print("the largest  number is:",largest_number)

# i = 1
# while i<= 50:
#     print(i," ", end="")
#     i+= 1

# number = int(input("enter the number:"))
# count = 1
# even = 0
# odd = 0
# while count<=number:
#     if count % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#         count += 1
# print("even=",even)
# print("odd=",odd)

# for counter in range(100):
#     print("counter:",counter)


# for counter in range(2, 8):
#     print("the value of counter is currently:",counter)



# for counter in range(2, 8, 3):
#      print("the value of counter is currently:",counter)

# power = 1
# for expo in range(16):
#     print(" 2 to the power of", expo, "is", power)
# power *= 2

# print("the break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         #break
#         continue
#     print("inside the loop:",counter)
# print("outside the loop:")


# var = 5
# print(var > 0)
# print(not(var <= 0))
# print(var != 0)
# print(not (var == 0))

# numbers = [10,5,7,2,1]
# print(numbers)
# print(type(numbers))

# print("first element content:", numbers[0])
# print("second element content:",numbers[1])
# print("third element content:", numbers[2])
# print("fourth element content:", numbers[3])
# print("fifth element content:", numbers[4])
  
# numbers[0] = 111
# print("numbers[0]:", numbers[0])
# print(numbers)

# numbers[1] = numbers[4]
# print(numbers) 
# print(len(numbers))
# del numbers[3]
# print(numbers)
# print(len(numbers))

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])
# # print(numbers[-5])
# # print(numbers[4])

# numbers = [1,2,3,4,5]
# print(numbers)
# print(len(numbers))
# del numbers[4]
# print(numbers)
# numbers[2] = 6
# print(numbers)
# print(numbers[-1])
# print(len(numbers//2))

# list = [1,2,3,4,5]
# print(list)
# list.append(6)
# print(list)
# list.insert(0, 10)
# print(list)

# print("1")
# print("2"*2)
# print("3"*3)
# print("4"*4)
# print("5"*5)
# print("6"*6)

# for temp in range(1,7):
#     print(str(temp)*temp)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])

# list = []
# for iterator in range(1,11):
#         list.append(iterator)
# print(list)

# list = []
# for iterator in range(10):
#         list.append(iterator+1)
# print(list)

# list = [10,20,30,40,50,60,70,80,90,100]
# for index in range(len(list)):
#     list[index] = list[index]+1
# print(list)

# list = [10,20,30,40,50,60,70,80,90,100]
# for index in range(len(list)):
#     list[index] += 1
# print(list)
    
# list = [10,20,30,40,50,60,70,80,90,100]
# sum = 0
# for element in range(len(list)):
#     sum += list[element]
# print(sum)

# my_list = [10,1,8,3,5]
# total = 0
# for element in my_list:
#     total += element
# print(total)

# variable1 = 1
# variable2 = 2
# print("Variable1:",variable1)
# print("Variable2:",variable2)
# variable1,variable2 = variable2,variable1
# print("Variable1:",variable1)
# print("Variable2:",variable2)

# list = [10,20,30,40,50,60,70,80,90,100]
# list[4],list[1] = list[1],list[4]
# print(list)

# list = [8,10,6,2,4]
# count = 0
# for i in range(len(list)):
#     for j in range(len(list)-1):
#         count += 1
#         if list[j] > list[j+1]:
#            list[j], list[j+1] = list[j+1], list[j]
# print(list)
# print(count)

# my_list = [8,10,6,2,4]
# swapped = True
# count = 0
# while swapped:
#     swapped = False
#     for i in range (len(my_list)-1):
#         count += 1
#         if my_list[i]>my_list[i+1]:
#             swapped = True
#             my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
# print(my_list)
# print(count)

my_list = [8,10,6,2,4]
my_list.sort()
print(my_list)





