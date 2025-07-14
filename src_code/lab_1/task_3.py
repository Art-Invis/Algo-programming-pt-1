import math
x = 2.735
z = 7.218

# Обчислення a, b, i, o, n, r
a = math.cos(x)
b = math.sin(x)
i = (z + x) / a
o = a * b
n = math.sqrt(abs(o))
r = 16 * z

# Виведення результату
result = (i + n) ** 2 + r
print(result)
