# Аты жөні Еренбай Айдын
# Тобы Тии-26-11 типо
# Нұсқа нөмірі 12
# Орындалған күні 10 / 12 / 2026

# 1 тапсырма Тізімді енгізу және шығару
# Пайдаланушыдан бір жолға бос орын арқылы кемінде бес бүтін сан енгізуді сұраңыз. Жолды split
# әдісімен бөліп, әр бөлікті int типіне түрлендіріп, тізімге сақтаңыз. Тізімді, ұзындығын, бірінші және
# соңғы элементін шығарыңыз.

text = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in text.split()]

print("List:", numbers)
print("Number of elements:", len(numbers))#5

if numbers:#5 10 20 30 60
    print("First:", numbers[0])#5 
    print("Last:", numbers[-1])#60
# 2 тапсырма Қосынды және орташа мән
# Тізім элементтерінің қосындысын for циклі арқылы есептеңіз. Орташа мәнді қосындыны
# элементтер санына бөлу арқылы табыңыз. Бос тізім үшін нөлге бөлу қатесін болдырмаңыз.
total = 0
for value in numbers:
 total += value
if numbers:# 5 10 20 30 60 
 average = total / len(numbers)
 print("Қосынды:", total)#125
 print(f"Орташа мән: {average:.2f}")#25.00
else:
 print("Тізім бос")
#  3 тапсырма Минимум және максимум
# min және max функцияларын қолданбай, ең кіші және ең үлкен элементті табыңыз. Алғашқы
# элементті бастапқы минимум және максимум ретінде алыңыз.
if numbers:#5 10 20 30 60
 minimum = numbers[0]
 maximum = numbers[0]
 for value in numbers[1:]:
    if value < minimum:
        minimum = value
    if value > maximum:
        maximum = value
 print("Минимум:", minimum)#5 
 print("Максимум:", maximum)#60
#  4 тапсырма Элементтерді санау
# Тізімдегі оң, теріс, нөл, жұп және тақ элементтердің санын анықтаңыз. 0 саны жұп екенін
# ескеріңіз.
positive = negative = zeros = even = odd = 0
for value in numbers: # 1 2 5 10 20 30 60 55
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        zeros += 1
    if value % 2 == 0:
        even += 1
    else:
        odd += 1
print("positiv",positive)#
print("negative",negative)
print("zeros",zeros)
print("even",even)
print("odd",odd)