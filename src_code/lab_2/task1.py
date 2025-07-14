import math

x = 0.1
h = 0.05

while x <= 0.7:
    if x < 0.2:
        y = math.log(3*x + 5, 5)
        print (f'{round(x, 2)} | {y}')
        x += h 
    elif x < 0.4:
        y = x**math.cos(x)
        print (f'{round(x, 2)} | {y}')
        x += h
    else:
        y = 1 / math.sin(math.log(x, 10))
        print (f'{round(x, 2)} | {y}')
        x += h
    print
print ('Done')
