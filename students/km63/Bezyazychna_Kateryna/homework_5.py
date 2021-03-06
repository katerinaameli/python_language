#task1----------------------------------------------------------------------
'''
Äàíû ÷åòûðå äåéñòâèòåëüíûõ ÷èñëà: x1, y1, x2, y2. Íàïèøèòå ôóíêöèþ
distance(x1, y1, x2, y2), âû÷èñëÿþùàÿ ðàññòîÿíèå ìåæäó òî÷êîé (x1,y1) è
(x2,y2). Ñ÷èòàéòå ÷åòûðå äåéñòâèòåëüíûõ ÷èñëà è âûâåäèòå ðåçóëüòàò ðàáîòû
ýòîé ôóíêöèè. 
'''

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
def distance(x1,y1,x2,y2):
    dis=((x2-x1)**2+(y2-y1)**2)**(1/2)
    return dis
print (distance(x1,y1,x2,y2))
    
#--------------------------------------------------------------------------


#task2---------------------------------------------------------------------
'''
Äàíî äåéñòâèòåëüíîå ïîëîæèòåëüíîå ÷èñëî a è öåëîe ÷èñëî n.
Âû÷èñëèòå a^n. Ðåøåíèå îôîðìèòå â âèäå ôóíêöèè power(a, n). 
'''

def neg_degree(a,n):
    if n<0:
        res=1/(a**abs(n))
        return res
    else:
        res=a**n
        return res
print(neg_degree(float(input()), float(input())))
    
#--------------------------------------------------------------------------


#task3---------------------------------------------------------------------
'''
Äàíî äåéñòâèòåëüíîå ïîëîæèòåëüíîå ÷èñëî a è öåëîå íåîòðèöàòåëüíîå ÷èñëî n.
Âû÷èñëèòå an íå èñïîëüçóÿ öèêëû, âîçâåäåíèå â ñòåïåíü ÷åðåç ** è ôóíêöèþ
math.pow(), à èñïîëüçóÿ ðåêóððåíòíîå ñîîòíîøåíèå a^n=a?a^(n-1).
Ðåøåíèå îôîðìèòå â âèäå ôóíêöèè power(a, n). 
'''

def power(a,n):
    res=1
    for i in range (1,n+1):
        res=res*a
    return res
print(power(float(input()),int(input())))

#--------------------------------------------------------------------------


#task4----------------------------------------------------------------------
'''
Íàïèøèòå ôóíêöèþ fib(n), êîòîðàÿ ïî äàííîìó öåëîìó íåîòðèöàòåëüíîìó n
âîçâðàùàåò n-e ÷èñëî Ôèáîíà÷÷è. Â ýòîé çàäà÷å íåëüçÿ èñïîëüçîâàòü öèêëû —
èñïîëüçóéòå ðåêóðñèþ. 
'''
   
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
            
#---------------------------------------------------------------------------
