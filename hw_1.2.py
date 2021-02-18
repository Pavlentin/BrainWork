n = 1000
a = []
count = 0
total = 0
for i in range(n):
    if count % 2 == 1:
        a.append(i)
    count += 1
a = [num ** 3 for num in a]
for i in a:
    if i % 7 == 0:
        total = total + i
a = [num + 17 for num in a]
total_1 = 0
for i in a:
    if i % 7 == 0:
        total_1 = total_1 + i
print(a)
print(total)
print(total_1)