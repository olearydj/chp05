# based on an example in 5.2.2
x = 5
print("T minus ", end="")

while x >= 1:
    print(f"{x}... ", end="")
    x = x - 1

print("\nLiftoff!")