"""
# Challenge

s = list(input("Enter x's and y's: "))

if s.count("x") == s.count("y"):
    print("True")
else:
    print("False")
"""

# Bonus Challenge

from collections import Counter

s = str(input("Enter x's and y's: "))
counts = Counter(s)

first_value = []
for i, j in enumerate(counts.values()):
    if i == 0:
        first_value.append(j)
    else:
        if j == first_value[0]:
            continue
        else:
            print("False")
            exit()

print("True")
