#Author:JTI 12/2/21

def sum_to(value):
    total = 0
    x = 0
    while x <= int(value):
        total += x
        x += 1
    return total


num = input("Enter an integer: ")
print(sum_to(num))

