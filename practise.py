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

# my_list = [8,10,6,2,4]
# my_list.sort()
# print(my_list)

# list = [8,10,6,2,4]
# print(list)
# list.reverse()
# print(list)

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
# print(list_1)

# my_list = [10,8,6,4,2]
# new_list = my_list[1:3]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[1:-1]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[-1:1]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[-5:3]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[:3]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[2:]
# print(new_list)

# my_list = [10,8,6,4,2]
# del my_list[1:3]
# print(my_list)
# del my_list[:]
# print(my_list)

# my_list = [0,3,12,8,2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")
# print(row)

# row = ["WHITE_PAWN" for i in range(8)]
# print(row)

# squares = [x**2 for x in range(10)]
# print(squares)

# squares = [x**2 for x in range(1,11)]
# print(squares)

# squares = [index**2 for index in range(1,11)]
# print(squaresb)

# twos = [2** index for index in range(8)]
# print(twos)

# squares = [index**2 for index in range(1,11)]
# odds = [element for element in squares if element % 2 != 0]
# print(odds)

# board = []
# for i in range(8):
#     row =["EMPTY" for i in range(8)]
#     board.append(row)
# # print(board)
# for index in board:
#  print(index)
 
# print(len(board))

# print(board[0][0])
# print("-----------")
# board[0][0] = "Rooks"
# board[0][7] = "Rooks"
# board[7][0] = "Rooks"
# board[7][7] = "Rooks"
# for element in board:
#    print(element)

# board[0][1] = "knight"
# board[0][6] = "knight"
# board[7][1] = "knight"
# board[7][6] = "knight"
 
# print("----------------")
# for element in board:
#    print(element)

# temps = [[0.0 for h in range(24)]for d in range(31)]
# temp1 = 19
# temp2 = 32
# count = 0
# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2   
#         count = 0
# for element in temps:
#     print(element)
  
# total = 0.0
# for day in temps:
#    total += day[11]

# average = total/31
# print("average temperature at noon:",average)

# highest = -100.0
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
# print("the highest temperature was:",highest)

# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days,"days were hot days in the month.")

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# print(rooms)

# rooms[1][9][13] = True

# rooms[1][9][1] = True

# vacancy = 0
# for room_number in range(20):
#     if not rooms[1][9][room_number]:
#         vacancy += 1
# print("vacancy in 3rd 15th floor of 3rd building",vacancy)

# def scope_test():
#     x = 123
# scope_test()
# print(x)

# def my_function():
#     print("Do I  know the variable?",var)

# var = 1
# my_function()
# print(var)

# def mult(x):
#     var = 7
#     return x*var
# var = 3
# print(mult(7))

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?",var)

# var = 1
# my_function()
# print(var)
 
# var = 2
# print(var)

# def return_var():
#     global var
#     var = 5
#     return var
# print(return_var())
# print(var)

# def my_function(n):
#     print("I got",n)
#     n += 1
#     print("I have",n)

# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("print #1:",my_list_1)
#     print("print #2:",my_list_2)
#     my_list_1 = [0,1]
#     print("print #3:",my_list_1)
#     print("print #4:",my_list_2)

# my_list_2 = [2,3]
# my_function(my_list_2)
# print("print#5:",my_list_2)

# def my_function(my_list_1):
#     print("print #1:",my_list_1)
#     print("print #2:",my_list_2)
#     del my_list_1[0]
#     print("print #3:",my_list_1)
#     print("print #4:",my_list_2)

# my_list_2 = [2,3]
# my_function(my_list_2)
# print("print#5:",my_list_2)

# def countdown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         print("going in rec:",number)
#         countdown(number-1)
#         print("out of rec:",number)
# print("starting recursion")        
# countdown(5) 
# print("completed recursion") 

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print("Factorial of 5 is:", factorial(5)) 

# my_tuple = (1,10,100)
# t1 = my_tuple + (1000,10000)
# t2 = my_tuple*3
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# my_tuple = (10,100,1000)
# my_tuple += (10000,100000)
# print(my_tuple)

# tuple_1 = (1,2,3)
# for elem in tuple_1:
#     print(elem)

# tuple_2 = (1,2,3,4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3 = (1,2,3,4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3*2
# print(tuple_4)
# print(tuple_5)

# my_tuple = tuple((1,2,"string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2,4,6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type)

# var = 123
# t1 = (1,)
# t2 = (2,)
# t3 = (3, var)
# t1, t2, t3 = t2, t3, t1
# print(t1,t2,t3)
# print(type(t1),type(t2),type(t3))

# dictionary = {"cat":"chat","dog":"chien","horse":"cheval"}
# phone_number = {'boss':123456789,'suzy':987654321}
# empty_dictionary = {}
# print(dictionary)
# print(type(dictionary))
# print((phone_number))
# print(type(phone_number))
# print(empty_dictionary)
# print(type(empty_dictionary))
# print(dictionary['cat'])
# print(phone_number['suzy'])
# # print(phone_number['president'])

# words = ['cat','lion','horse']
# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print("----",word,"is not in dictionary","----")

#     print(dictionary.keys())
#     for key in dictionary.keys():
#          print(key,"->",dictionary[key])

#     for key, value in dictionary.items():
#         print(key,"->",value)
#         print(dictionary.value())
#         for value in dictionary.values():
#             print(value)

# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
#     }
# print ("poly_eng_dictionary:",pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()
# print("copy_dictionary:",copy_dictionary)
# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)

# phonebook = {}
# print(phonebook)
# phonebook["Adam"] = 98765432
# print(phonebook)
# del phonebook["Adam"]
# print(phonebook)

# pol_eng_dictionary = {"kwiat":"flower"}
# pol_eng_dictionary.update(
#     {
#         "gleba":"soil"
#     })
# print(pol_eng_dictionary)
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)

# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
# }
# if "zamek1" in pol_eng_dictionary:
#     print("yes! zamek1 is presnet in dictionary")
# else:
#     print("no! zamek1 is not present in the dictionary")

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary
# print(pol_eng_dictionary)

# sd = {}
# while True:
#     name = input("enter student's name:")
#     if name == "":
#         break
#     score = int(input(f"enter {name}'s score:"))
#     if score not in range(1,11):
#         break
#     if name in sd:
#         sd[name] += (score, )
#     else:
#         sd[name] = (score, )
# print(sd)
# for name, mark in sd.items():
#     sum = 0
#     for m in mark:
#         sum += m
#         print(name,"->",sum/len(mark))

# class ThisIsMyFirstClass:
#     name = "himani"
#     age = 20
#     def getName(self):
#         print(self.name)
# firstobject = ThisIsMyFirstClass()
# print(firstobject) 
# firstobject.getName()
# print(firstobject.name)

# class student:
#     def _init_(self):
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""
# himani = student()
# print(himani)

# himani.name = "himani sabre"
# himani.age = 20
# himani.gender = "female"
# himani.grade = "12th"

# print(himani.name)
# print(himani.age)
# print(himani.gender)
# print(himani.grade)

# class student:
#     def __init__(self,name,age,gender,grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade
#     def printDetails(self):
#         print("name:", self.name)
#         print("age:", self.age)
#         print("gender:", self.gender)
#         print("grade:", self.grade)
# himani = student("himani sabre",20,"female","12th")
# print(himani)
# himani.printDetails()

# class classy:
#     def method(self,par):
#         print("method",par)
# obj = classy()
# obj.method(1)

# class classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)
# obj = classy()
# obj.var = 3
# obj.method()

# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy
# sun = Star("sun","milky way")
# print(sun)

# class star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
# sun = star("sun","milkyway")
# print(sun)

# class Vehicle:    
#     pass
# class LandVehicle(Vehicle):   
#      pass
# class TrackedVehicle(LandVehicle):    
#     pass
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:    
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")   
# print()

# class Super:    
#     supVar = 1
# class Sub(Super):    
#     subVar = 2
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# class Super:
#     def __init__(self):
#         self.supVar = 11
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
# obj = Sub()
# print(obj.subVar) 
# print(obj.supVar)

class Level1:
    variable_1 = 100
    def __init__(self):
       self.var_1 = 101
    def fun_1(self):
       return 102
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
       super().__init__()
       self.var_2 = 201
    def fun_2(self):
       return 
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
       super().__init__()
       self.var_3 = 301
    def fun_3(self):
        return 
obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2()) 
print(obj.variable_3, obj.var_3, obj.fun_3())

        
    

        
        
        





        
























































  
  