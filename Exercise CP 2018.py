############# CNC Info 2018 ##############
# Prefix
def prefix(M, S):
    if len(M) > len(S):
        return False
    elif not M or not S:
        return None
    elif S.startswith(M):
        return True

S = input("Enter a string: ")
M = input("Enter the second string: ")
if prefix(M, S):
    print(f"The string {M} is a prefix of the string {S}")
elif prefix(M, S) is None:
    print("The strings are empty")
else:
    print(f"The string {M} is not a prefix of the string {S}")

# Suffixes
def list_suffixes(S):
    l = []
    for i in range(len(S)):
        l.append((S[i:], i))
    return l

S = 'TATCTAGCTA'
print(list_suffixes(S))
print("----------------------------------")

# Sort list
def sort_list(L):
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i][0] > L[j][0]:
                L[i], L[j] = L[j], L[i]
    return L

print(sort_list(list_suffixes(S)))
print("----------------------------")

# Binary search
def search(M, L):
    position = None
    for i in range(len(L)):
        if L[i][0].startswith(M):
            position = L[i][1]
    if position is None:
        return "None"
    return position

print(search(M, sort_list(list_suffixes(S))))

# Homogeneous
def homogeneous(l):
    for i in l:
        if type(i) != type(l[0]):
            return False
    return True

l = [0.2, 0.01, 1.6, 77.8, 102.15]
print(homogeneous(l))

# Minimum
def minimum(l):
    min_val = l[0]
    for i in range(len(l)):
        if l[i] < min_val:
            min_val = l[i]
    return min_val

print(minimum(l))

# Maximum
def maximum(l):
    max_val = l[0]
    for i in range(len(l)):
        if l[i] > max_val:
            max_val = l[i]
    return max_val

print(maximum(l))
