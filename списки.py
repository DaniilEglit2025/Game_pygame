a = [1, 2, 3]
print(a)
print(a[1])

a.append(99)
print(a)

a.pop(1)
print(a)

a[1] = 10
print(a)

print(len(a))

for i in range(len(a)):
    print(i)