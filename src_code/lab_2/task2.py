import math
step = 0.1
x = 1.1

while (x <= 2):

    k = 1
    delta = 0.001

    y = 0
    while True:
        el = (1 / 2**k) * math.sin(x / 2**k)
        if abs(el) < delta:
            break
        y += el
        k += 1
        
    print(f'{round(x,3)} | sum= {y}')
    x += step
