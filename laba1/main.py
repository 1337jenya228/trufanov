import string as str
import math as m

print('Для анлиза надежности пароля будет использоваться латинский алфавит')
password = input('Ведите пароль: ')
speed_password = int(input('Введите скорость подбора пароля: '))
count_failed = int(input('Введите количество попыток подбора пароля после которого будет сделана пауза: '))
pause_time = int(input('Введите длительность паузы в секундах: '))
special_characters = str.punctuation

digit = False
lower = False
upper = False
spec_char = False
space = False
power = 0

for i in range(len(password)):
    if digit != True:
        if password[i].isdigit():
            digit = True
power += 10
if lower != True:
    if password[i].islower():
        lower = True
power += 26
if upper != True:
    if password[i].isupper():
        upper = True
power += 26
if space != True:
    if password[i].isspace():
        space = True
power += 1
if spec_char != True:
    for j in range(len(special_characters)):
        if password[i] == special_characters[j]:
            spec_char = True
            power += 32
            break
    j = 0

password_length = len(password)
password_power = pow(power, password_length)
password_time_without_pause = int(password_power / speed_password)
password_time_seconds = password_time_without_pause + (password_power / count_failed) * pause_time

if password_power % count_failed == 0:
    password_time_seconds -= pause_time

years = int(password_time_seconds // 60 // 60 // 24 // 365)
mounths = int((password_time_seconds // 60 // 60 // 24 // 30) % 12)
days = int((password_time_seconds // 60 // 60 // 24) % 30)
hours = int((password_time_seconds // 60 // 60) % 24)
minutes = int((password_time_seconds // 60) % 60)
seconds = m.floor(password_time_seconds % 60)

print('Длина пароля = ', password_length, 'символам')
print('Мощность алфавита = ', power)
print('Мощность пространства = ', password_power)
print('Время подбора пароля без учета пауз ', password_time_without_pause, ' секунд')
print('Подбор пароля займет ', years, ' лет ', mounths, ' месяцев ', days, ' дней ', hours, ' часов ', minutes,
      ' минут ', seconds, 'секунд')
