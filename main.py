# define functions add, sub, div, mult
# print options to user
# ask for values/inputs
# call functions
# while loop to continue until user wants to exit

def add(a,b):
    result = a+b
    print(f' {a} + {b} = {result}')

def sub(a,b):
    result = a-b
    print(f' {a} - {b} = {result}')

def mult(a,b):
    result = a*b
    print(f' {a} * {b} = {result}')

def div(a,b):
    result = a/b
    print(f' {a} / {b} = {result}')



while True:
    print(f' A. Addition \n B. Subtraction \n C. Multiplation \n D. Division \n E. Exit')

    choice = input(f' Please select your choice: ').lower()

    if choice == 'a':
        print('Addition')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        add(a,b)

    elif choice == 'b':
        print('Subtraction')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        sub(a,b)

    elif choice == 'c':
        print('Multiplication')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        mult(a,b)

    elif choice == 'd':
        print('Division')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        div(a,b)

    else:
        print('Exit')
        quit()




