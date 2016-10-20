﻿#task1------------------------------------------------------------
"""
Дано два цілих числа. Вивести найменше з них
"""

a,b - integer numbers
a = int(input())
b = int(input())
if (a < b):
    print(a)
else: 
    print(b)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Вивести результат функції sign(x), що визначається наступним чином:
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..
"""

def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

x=int(input())
print(sign(x))

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано три цілих числа. Вивести найменше з них.
"""

x,y,z - integer numbers
x = int(input())
y = int(input())
z = int(input())
    if x>=y > z:
        print(z)
    elif y>x > z:
        print(z)
    elif  x>=z > y:
        print(y)
    elif  z>x > y:
        print(y)
    else:
        print(x)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".
Рік високосний, якщо виконується хоча б одна з умов:
рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі
"""

a=input(int())
    if (a%4==0) and (a%100!=0):
        print ("LEAP")
    elif a%400==0:
        print("LEAP")
    else :
        print("COMMON")

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
"""

#a,b,c - numbers
a=input()

b=input()

c=input()

    if a==b and b==c:
    
        print(3)
    
elif a==b or b==c or a==c:
    
        print(2)
    
else:
    
        print(0)


#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
"""

a,b,c,d - coordinates
a=input()

b=input()

c=input()

d=input()
    
if a==c or b==d:
    
        print ("Yes")
    
else:
    
        print("No")

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""

#a,b,c,d- coordinates

a,b,c,d=[int(input()) for i in range(4)]

print('Yes'if a+b%2 == c+d%2 else 'No')


#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

a,b,c,d=[int(input()) for i in range(4)]

print('Yes'if abs(c-a)<2 and abs(d-b)<2 and (a!=c or b!=d) else 'No')


#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1,y1,x2,y2=[int(input()) for i in range(4)]

print('Yes'if abs(x2-x1)==abs(y2-y1) and x2!=x1 else 'No')

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1,y1,x2,y2=[int(input()) for i in range(4)]
rook, bishop = False, False
if  abs(x2-x1)==abs(y2-y1) and x2!=x1:
    bishop = True
if (x1==x2 and y1!=y2) or (x1!=x2 and y1==y2):
    rook=True
print('Yes' if rook or bishop else 'No')

#-----------------------------------------------------------------	


#task11------------------------------------------------------------
"""
Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1,y1,x2,y2=[int(input()) for i in range(4)]

print('Yes'if (abs(x2-x1)==2 and abs(y2-y1)==1) or (abs(x2-x1)==1 and abs(y2-y1)==2) else 'No')


#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
"""

n,m,k=[int(input()) for i in range(3)]

print('Yes'if n*m>k and (k%n==0 or k%m==0) else 'No')



#-----------------------------------------------------------------