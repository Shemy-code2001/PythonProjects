#NESTED LOOPS / DRAWING:
#Length: number of rows
#Width: number of columns
#EXAMPLES:
l = int(input("Enter the length: "))
c = int(input("Enter the width: "))
for i in range(l):  # rows //5
    for j in range(c):  # columns //5
        print("*", end="")
    print()
#############################"
l = int(input("Enter the length: "))
c = int(input("Enter the width: "))
for i in range(l):  # rows
    print("*" * c)
#EMPTY SQUARE:
l = int(input("Enter the length: "))
c = int(input("Enter the width: "))
for i in range(l):
    if i == 0 or i == l - 1:
        for j in range(c):
            print("*", end=" ")
    else:
        for j in range(c):
            if j == 0 or j == c - 1:
                print("*", end=" ")
            else:
                print(end="  ")
    print()  # for line break
# TRIANGLES:
#height: the rows = In a drawing, what happens in each row varies, either increasing or decreasing (the final value of the range function in the second loop is always based on (i = the counter of the 1st loop)
#increase: range(i) or range(i+1)
#decrease: range(h-i) or range(h-i-1)
h = int(input("Enter the height of the triangle: "))
for i in range(h):
    for j in range(i + 1):
        print("*", end="")
    print()
#inverted triangle:
h = int(input("Enter the height of the triangle: "))
for i in range(h):
    #loop to draw spaces (increase)
    for j in range(i):
        print(" ", end="")
    #loop to draw triangles (decrease)
    for j in range(h - i):
        print("*", end="")
    print()
    ############################################
l = int(input("Enter the length: "))
c = int(input("Enter the width: "))
for i in range(l):
    for j in range(c):
        print("-", end="")
    print()
    ###########################################
l = int(input("Enter the length: "))
c = int(input("Enter the width: "))
for i in range(l):
    if i == 0 or i == l - 1:
        for j in range(c):
            print("*", end=" ")
    else:
        for j in range(c):
            if j == 0 or j == c - 1:
                print("*", end=" ")
            else:
                print(end="  ")
    print()

    
