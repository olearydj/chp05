# based on 5.2.4 - Digits
num = int(input("*** Enter an integer value: "))

while num > 0:
    print(num % 10)
    num = num // 10

# what happens if I forget to update num?