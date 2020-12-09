  #Sign your name:_Gerardo Lopez_______________

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
    print("The total is:", total)
'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
x = 0
for i in range(50):
    x = x + 2
    print(x)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
number = random.randint(1,10)
print(number)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
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

print("The total is:", total)


