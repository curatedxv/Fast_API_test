a = b = c = [1, 2, 3]
b.append(4)
c.pop(2)
a.extend(c)
print(a)