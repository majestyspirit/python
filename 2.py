def number(n):
    return (i for i in range(1, n + 1, 2))


num = number(int(input()))

print(type(num))

for a in num:
    print(a)
