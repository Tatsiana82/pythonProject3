"""#2.1
health_level = int(input("Enter a level of health"))
if health_level <= 0:
    print(False)
else:
    print(True)
#2.2
num = int(input("Enter a number"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#2.3
year = int(input("Enter a year"))
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Невисокосный")
#2.4

text = input("Enter your text")
num = int(input("Enter a number"))
for i in range(num):
   print(text)"""

'''try:
    num1 = int(input('Пожалуйста, введите первое число: '))
    num2 = int(input('Пожалуйста, введите второе число: '))
except ValueError as e:
    print(f'Введенное значение не является числом: {e}')
    sys.exit()
operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
if operator not in '+-*/%':
    print("Вы ввели не правильный оператор!")
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')'''


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
operator = input("Enter operator")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "%":
     print(num1 % num2)
if operator not in "+-*/%":
    print("Wrong operator")
    sys.exit()
result = 0
if num2 == 0 and operator == "/":
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Division is forbidden")
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')






