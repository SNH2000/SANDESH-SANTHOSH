a = int(input("Enter the number: "))
for i in range(a):
    print(2 * i + 1, end=", " if i < a - 1 else "")
