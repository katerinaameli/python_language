#task1------------------------------------------------------------
"""
Дано два цілих числа. Вивести найменше з них.
"""

a = int(input("Please enter first number "))
b = int(input("Please enter second number "))

if a < b:
	print("Number ", a, " less than the number ", b)
elif b < a:
	print("Number ", b, " less than the number ", a)	
else:
	print("Number ", a, " equals ", b)	

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0.
"""

def sign(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	elif x == 0:
		return 0	

x = int(input("Please enter the number "))
print(sign(x))			

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано три цілих числа. Вивести найменше з них.
"""

a = int(input("Please enter first number "))
b = int(input("Please enter second number "))
c = int(input("Please enter third number "))


if (a > b) and (a > c):
	print(a, " is the largest number")
elif (b > a) and (b > c):
	print(b, " is the largest number")
elif (c > a) and (c > b):
	print(c, " is the largest number")
else:
	print(a, " = ", b, " = ", c)


#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".
Рік високосний, якщо виконується хоча б одна з умов:
рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі
"""

y = int(input("Please enter the year "))

if (y < 0): 
	print("Invalid value, try again")
else:
	if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 != 0):
		print("LEAP")
	else:
		print("COMMON")		

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. 
Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
"""

a = int(input("Please enter first number "))
b = int(input("Please enter second number "))
c = int(input("Please enter third number "))

if (a == b) and (b == c):
	print("3")
elif (a == b) or (b == c) or (a == c):
	print("2")
else:
	print("0")		

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. 
Визначити, чи може тура перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))

if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:	
	if ((x1 == x2) and (y1 != y2)) or ((y1 == y2) and (x1 != x2)):
		print("YES")
	else:
		print("NO")	

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))


if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:
	if (abs(x1 - x2) + abs(y1 - y2)) % 2 == 0:
		print("YES")
	else:
		print("NO")	

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. 
Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))


if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:
	if (abs(x1 - x2) == 1) or (abs(y1 - y2) == 1):
		print("YES")
	else:
		print("NO")	 

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. 
Визначити, чи може слон перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))

if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:
	if abs(x2-x1) == abs (y2-y1):
		print("YES")
	else:
		print("NO")

#write your answer here...

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. 
Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))

if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:
	if (abs(x2-x1) == abs (y2-y1)) or ((x1 == x2) and (y1 != y2)) or ((y1 == y2) and (x1 != x2)):
		print("YES")
	else:
		print("NO")

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Шаховий кінь рухається як літера L. 
Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. 
Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

x1 = int(input("Please enter first coordinate "))
y1 = int(input("Please enter second coordinate "))
x2 = int(input("Please enter third coordinate "))
y2 = int(input("Please enter fourth coordinate "))


if (x1 < 1) or (x1 > 8) or (y1 < 1) or (y1 > 8) or(x2 < 1) or (x2 > 8) or(y2 < 1) or (y2 > 8):
	print("Invalid values, try again")
else:
	if ((abs(x1-x2) == 2) and (abs(y1 - y2) == 1)) or ((abs(y1-y2) == 2) and (abs(x1 - x2) == 1)):
		print("YES")
	else:
		print("NO")	

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Шоколад має форму прямокутника, розділеного на n×m клітин. 
Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. 
Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. 
Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
"""

n = int(input("Please enter n "))
m = int(input("Please enter m "))
k = int(input("Please enter k "))

if (n < 0) or (m < 0) or (k < 0):
	print("Invalid value, try again")
else:	
	if (k % m == 0) or (k % n == 0):
		print("YES")
	else:
		print("NO")	

#-----------------------------------------------------------------