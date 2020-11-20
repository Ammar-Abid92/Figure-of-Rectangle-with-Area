# EXERCISE 1 , QUESTION # 3
a = int(input("enter length of rectangle: "))
b = int(input("enter height of rectangle: "))
Area = a * b
print("The area of rectangle is: ", Area, "Sq.Units")

for length in range(0, a+4):
    print('_', end="")
print("")
for height in range(0, b):
    print('|', a*" ", "|")

for length in range(a+4):
    print('-', end="")


