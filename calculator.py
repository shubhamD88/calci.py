 # calculetor

a = int(input('Enter your first value : '))
b= int(input('Enter your second value : '))
c = input('input opretion symbol ')

if c == '+' :
    print(a + b)
elif c == '*':
    print(a * b)
elif c == '%' :
    print(a % b)
elif c == '-':
    print(a - b)
elif c == '/' :
    print(a / b)
else:
    print( 'invalid input')
