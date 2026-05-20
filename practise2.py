# print("testing comit changes")
list = [8,10,6,2,4]
for i in range(len(list)):
    for j in range(len(list)-1):
     if list[j] > list[j+1]:
       list[j], list[j+1] = list[j+1], list[j]
       