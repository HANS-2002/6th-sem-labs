# WAP to check whether an input integer is perfect number or not.
n = int(input("Enter n: "))

sum = 0
for num in range(1, n):
    if n % num == 0:
        sum += num

if sum == n:
    print(f"{n} is perfect!")
else:
    print(f"{n} is not perfect!")