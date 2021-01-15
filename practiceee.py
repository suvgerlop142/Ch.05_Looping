total = 0
pos = 0
neg = 0
zero = 0
for i in range(7):
    x = int(input("Enter a number: "))
    total = total + x
    if x > 0:
        pos = pos + 1
    elif x < 0:
        neg = neg + 1
    else:
        zero = zero + 1
print("Number of postive entries: ", pos)
print("Number of negative entries: ", neg)
print("Number of entries equal to zero", zero)