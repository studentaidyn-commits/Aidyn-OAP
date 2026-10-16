                # Еренбай Айдын
                # Тии-26-11 типо
                    #1-нұсқа
                  #1 тапсырма

# n = int(input("1 "))
# while n <= 0:
#     n = int(input("negative "))
# print(n)

                 #2 тапсырма
# n = int(input("1 "))
# i = 1
# s = 0
# while i <= n:
#     s += i
#     i += 1
# print(s)

              #3 тапсырма

# n = int(input("1 "))
# if n < 0:
#     print("negative")
# else:
#     fact = 1
#     i = 1
#     while i <= n:
#         fact *= i
#         i += 1
#     print("Факториал:", fact)

              #4 тапсырма

positive = 0
negative = 0
total = 0
count = 0
n = int(input("0 "))
while n != 0:
    total += n
    count += 1
    if n > 0:
        positive += 1
    else:
        negative += 1
    n = int(input("0 "))
print("positive",positive,"negative",negative,"kosu",total)
if count>0:
  print("orta",total/count)
