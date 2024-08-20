# Series Exercises on Two-Dimensional Lists

# Exercise 1:
#a

def fill_list(num_rows, num_cols):
    if num_cols <= 0 or num_rows <= 0:
        return False
    rows = []
    for i in range(num_rows):
        cols = []
        for j in range(num_cols):
            num = float(input("Enter a number: "))
            cols.append(num)
        rows.append(cols)
    return rows

#b
def display(lst):
    for i in lst:
        for j in i:
            print(j)

#c
def sum_list(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j
    print(f"The sum of all elements in the list is: {total}")

# Method 2
def sum_list(lst):
    total = 0
    for i in lst:
        total += sum(i)
    print(f"The sum of all elements in the list is: {total}")

# Method 3:
def sum_list_3(lst):
    return sum(sum(i) for i in lst)

#d
def count_positive(lst):
    positive_count = 0
    for i in lst:
        for j in i:
            if j > 0:
                positive_count += 1
    return positive_count

#e
def sum_elements(lst):
    sum_pos = 0
    sum_neg = 0
    for i in lst:
        for j in i:
            if j > 0:
                sum_pos += j
            else:
                sum_neg += j
    print(f"The sum of negative numbers is {sum_neg} and the sum of positive numbers is {sum_pos}")
    return sum_pos, sum_neg

#f
def find_max_value(lst):
    max_val = lst[0][0]
    position = (0, 0)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] > max_val:
                max_val = lst[i][j]
                position = (i, j)
    print(f"The maximum value is {max_val} at position {position}")
    return max_val, position

# Method 2:
def max_value(lst):
    return max(max(row) for row in lst)

#g
def reverse_row(lst):
    index = int(input("Enter the row index: "))
    lst[index].reverse()
    return lst

# Main program:
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
matrix = fill_list(num_rows, num_cols)
display(matrix)
sum_list(matrix)
positive_count = count_positive(matrix)
print("The positive elements count is:", positive_count)
sum_pos, sum_neg = sum_elements(matrix)
print("The sum of positive elements is:", sum_pos)
print("The sum of negative elements is:", sum_neg)
max_val, max_pos = find_max_value(matrix)
print("The largest value is:", max_val, "at position", max_pos)

# Exercise 2:
N = int(input("Enter the number of rows and columns: "))
matrix_2D = []

for i in range(N):
    row = []
    for j in range(N):
        num = int(input(f"Enter a number for row {i + 1}, column {j + 1}: "))
        row.append(num)
    matrix_2D.append(row)

sum1 = 0
for i in range(N):
    sum1 += matrix_2D[i][i]

sum2 = 0
for i in range(len(matrix_2D)):
    s = 0
    for j in range(len(matrix_2D[i])):
        s += matrix_2D[i][j]
    sum2 += s

sum3 = 0
for i in range(len(matrix_2D)):
    for j in range(len(matrix_2D[i])):
        if j == i:
            sum3 += matrix_2D[i][j]

if sum1 == sum2 == sum3:
    print("The matrix_2D is a magic square.")
else:
    print("The matrix_2D is not a magic square.")

# Method 2:
# Exercise 2: MAGIC SQUARE

m = [[2, 45, 56],
     [2, 4, 3],
     [23, 4, 45]]

def is_magic_square(m):
    magic_sum = sum(m[0])
    # Check rows
    for row in m:
        if sum(row) != magic_sum:
            return False
    # Check columns
    for i in range(len(m)):
        col_sum = 0
        for j in range(len(m)):
            col_sum += m[j][i]
        if col_sum != magic_sum:
            return False
    # Check main diagonal
    diag_sum = 0
    for i in range(len(m)):
        diag_sum += m[i][i]
    if diag_sum != magic_sum:
        return False
    # Check secondary diagonal
    sec_diag_sum = 0
    for i in range(len(m)):
        sec_diag_sum += m[i][len(m) - i - 1]
    if sec_diag_sum != magic_sum:
        return False
    return True

# Main program
matrix = []
with open("magic.txt", "r") as f:
    for line in f:
        row = line.strip().split(",")
        matrix_row = [int(num) for num in row]
        matrix.append(matrix_row)

# Exercise 4:
matrix_2D = []
num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows):
    row = []
    num_cols = int(input("Enter the number of columns: "))
    for j in range(num_cols):
        num = int(input("Enter a number: "))
        row.append(num)
    matrix_2D.append(row)

for row in matrix_2D:
    print(row)

is_upper_triangular = True
for i in range(1, len(matrix_2D)):
    for j in range(i):
        if matrix_2D[i][j] != 0:
            is_upper_triangular = False
            break

if is_upper_triangular:
    print("The matrix_2D is an upper triangular matrix.")
else:
    print("The matrix_2D is not an upper triangular matrix.")

# Exercise 3:
matrix_2D = []
num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows):
    row = []
    num_cols = int(input("Enter the number of columns: "))
    for j in range(num_cols):
        num = int(input("Enter a number: "))
        row.append(num)
    matrix_2D.append(row)

points_cols = []
for i in range(num_rows):
    min_row = min(matrix_2D[i])
    for j in range(num_cols):
        max_col = max(matrix_2D[k][j] for k in range(num_rows))
        if matrix_2D[i][j] == min_row and matrix_2D[i][j] == max_col:
            points_cols.append((i, j))

print("The saddle points of the matrix are:")
for point in points_cols:
    print(point)
