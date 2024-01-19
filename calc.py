from platform import architecture


def sum():
    s = input("Введите числа через пробел\n").split() 
    summ = 0
    for i in range(len(s)):
        s[i]= int(s[i])

    for i in range(len(s)):
        summ += s[i]

    print(summ)

def del():
    s = input("Введите числа через пробел\n").split() 
    summ = 0
    for i in range(len(s)):
        s[i]= int(s[i])

    for i in range(len(s)):
        summ /= s[i] 

    print (summ)       

def razn():
    s = input("Введите числа через пробел\n").split()
    summ = 0
    for i in range(len(s)):
        s[i]= int(s[i])
    summ = s[0]
    for i in range(1, len(s)):
        summ -= s[i]
    
    print(summ)

def srar():
    s = input("Введите числа через пробел\n").split()
    summ = 0
    for i in range(len(s)):
        s[i]= int(s[i])
    for i in range(len(s)):
        summ += s[i]
    sr = summ / len(s)
    print(sr)

def fact():
    s = input("Введите число\n")
    summ = 1
    s= int(s)
    for i in range(1, s+1):
        summ *= i
    print(summ)

a = 0

while(a != 11):
    try:
        a = int(input("1) Сложение\n2) Вычитание\n3) Среднее арифметическое\n4) Факториал\n5) Деление\n11 - выход\n"))
        if a == 1:
            sum()
        elif a == 2:
            razn()
        elif a == 3:
            srar()
        elif a == 4:
            fact()
        elif a == 5:
            del()    
        elif a == 11:
            break
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    except ValueError:
        print("Ошибка при переведении в число. Попробуйте не вводить буквы или другие символы.")
    except ArithmeticError:
        print("Арифметическая ошибка")
