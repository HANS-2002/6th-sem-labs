# WAP to calculate the factorial of a given number
def findFac():
    n = int(input("Enter number to find factorial: "))
    prod = 1
    for num in range(1, n + 1):
        prod *= num
    print(f"{n}! = {prod}")

findFac()