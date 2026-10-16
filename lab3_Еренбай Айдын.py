                # Еренбай Айдын
                # Тии-26-11 типо
                    #1-нұсқа

                  #1 тапсырма
# a = int(input("1 "))
# b = int(input("2 "))
# c = int(input("3 "))
# if a==b and b==c:
#   print("Тең",a,b,c)
# elif a >= b and a >= c:
#     print("Ең үлкен сан:", a) 
# elif b >= a and b >= c:
#     print("Ең үлкен сан:", b)
# else:
#     print("Ең үлкен сан:", c)
  
                 #2 тапсырма

# a= int(input("балл "))
# b= int(input("қатысу % "))
# if a>=51 and b>=70:
#   print("өтті")
# else:
#   print("өтпеді")

              #3 тапсырма

# year= int(input("Жыл : "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Кібісе жыл")
# else:
#     print("Кібісе жыл емес")

              #4 тапсырма

a = float(input("1 "))
b = float(input("1 "))
c = input("+, -, *, / ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("нөлге бөлуге болмайды")
else:
    print("error")
