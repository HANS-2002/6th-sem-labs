# WAP to print all odd and even numbers separately within a given range. The range is input through user.
l = int(input("Enter left of range: "))
r = int(input("Enter right of range: "))
odd = []
even = []
for num in range(l, r + 1):
    if num & 1:
        odd.append(num)
    else:
        even.append(num)

print(f"Even number -> {even}")
print(f"Odd number -> {odd}")