list = []
n = int(input("Enter no. of numbers: "))

list.append(int(input("Enter First number: "))) 

for i in range(1, n):
    list.append(int(input("Enter next number: ")))
 
max = list[0]
for i in range(1, n):
    if(max < list[i]):
        max = list[i]

min = list[0]
for i in range(1, n):
    if(min > list[i]):
        min = list[i]

sum = 0
for i in range(0, n):
    sum += list[i]
average = sum/n

print("maximum of the numbers is: ", max)
print("minimum of the numbers is: ", min)
print("average of the numbers is: ", average)