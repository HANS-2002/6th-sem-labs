# WAP to calculate sum of digits of a number
n = input("Enter a number: ")
sum = 0
for num in n:
    sum += ord(num) - ord('0')
print(f"Sum of digits of {n} = {sum}")