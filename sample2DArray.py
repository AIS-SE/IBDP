# This program takes a 3x3 matrix as input and calculates the sum of each column and the average of each row.
numbers = [[0 for i in range(3)] for j in range(3)]
sum = 0
s=0
for i in range(3):
    for j in range(3):
        numbers[i][j] = int(input("Enter a value: "))
# traverse the array
for i in range(3):
    for j in range(3):
        # calculate the sum per column
        sum = sum + numbers[j][i]
    print(sum)
sum = 0
# traverse the array
for i in range(3):
    for j in range(3):
        # calculate the average per row
        s = s + numbers[i][j]
    avg = s/3
    print(avg)
    s=0
