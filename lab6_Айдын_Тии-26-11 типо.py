#1 тапсырма Қарапайым функция
#Санның квадратын қайтаратын square(number) функциясын жазыңыз. Функцияны 5, 0 және -4
#аргументтерімен шақырыңыз.
def square(number):
 return number ** 2
print(square(5))
print(square(0))
print(square( - 4))
#Күтілетін нәтиже: 25, 0, 16.
#2 тапсырма Бірнеше параметр
#Үш санның арифметикалық ортасын қайтаратын average(a, b, c) функциясын жазыңыз. Нәтижені
#екі ондық таңбаға дейін шығарыңыз. Кемінде үш тест қолданыңыз.
def average(a, b, c):
 return (a + b + c) / 3
result = average(4, 7, 10)
print(f"average: {result:.2f}")
print(average(45,14,95))
print(average(85,95,100))
print(average(7,8,9))
#Күтілетін нәтиже: average: 7.00, 51.336, 93.333, 8.0
#3 тапсырма Шартты функция
#Балл қабылдап, 50 немесе одан жоғары болса True, әйтпесе False қайтаратын is_passed(score)
#функциясын жазыңыз. 49, 50 және 100 мәндерін тексеріңіз. Диапазоннан тыс балл енгізілгенде
#жеке хабар көрсетіңіз.
def is_passed(score):
 if score < 0 or score > 100:
    return None
 return score >= 50
print(is_passed(49))
print(is_passed(50))
print(is_passed(100))
#Күтілетін нәтиже: False, True, True
#4 тапсырма Әдепкі параметр
def power(number, exponent=2):
  return number**exponent
print(power(6))
print(power(2,5))
print(power(-3,3))
#Күтілетін нәтиже: 36, 32, -27
#5 тапсырма Декомпозиция
def subtotal(price, quantity):
 return price * quantity
def discount_amount(amount, rate):
 return amount * rate
def final_price(price, quantity, rate=0):
 amount = subtotal(price, quantity)
 return amount - discount_amount(amount, rate)
print(final_price(2500, 3, 0.10)) # 6750.0
print(final_price(1500,3,0)) #4500
print(final_price(3500,1,100)) #-346500

#4 Жеке нұсқалар
#12 нұсқа
def soma(amount, currency):
 return None
def course(currency, change):
 return None
def comisia(soma, course,comisiaa):
 return (soma*course)-(soma*course)*comisiaa
print(comisia(100,453.93 ,0.05))#43123.35
