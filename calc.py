print('Введите переменную 1')
a = float(input()) #переменная 1
print('Введите переменную 2')
b = float(input()) #переменная 2
print('Введите действие (+, -, /, *, mod, div, pow)')
c = str(input()) #Само действие

'''
mod - взятие остатка от деления
pow - возведение в степень
div - целочисленное деление
'''

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
