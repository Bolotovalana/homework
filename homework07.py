# Task 2
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0



# 1. Дюймы в сантиметры

def inches_to_cm(digit):
    return float(digit * 2.54)


# 2. Сантиметры в дюймы
def cm_to_inches(digit):
    return float(digit / 2.54)


# 3. Мили в километры
def ml_to_km(digit):
    return float(digit * 1.60934)


# 4. Километры в мили

def km_to_ml(digit):
    return float(digit / 1.60934)


# 5. Фунты в килограммы

def pound_to_kg(digit):
    return float(digit * 0.453592)


# 6. Килограммы в фунты

def kg_to_pound(digit):
    return float(digit / 0.453592)


# 7. Унции в граммы
def ounce_to_gr(digit):
    return float(digit * 28.349)


# 8. Граммы в унции

def gr_to_ounce(digit):
    return float(digit / 0.453592)


# 9. Галлон в литры

def gl_to_ltr(digit):
    return float(digit * 3.78)


# 10. Литры в галлоны

def ltr_to_gl(digit):
    return float(digit / 0.453592)


# 11. Пинты в литры

def pint_to_ltr(digit):
    return float(digit * 0.473176)


# 12. Литры в пинты

def ltr_to_pint(digit):
    return float(digit / 0.473176)


while True:
    a = int(input("введите число вашего выбора от 0 до 12 "))

    if a == 0 or a < 0 or a > 12:
        break

    if a == 1:
        print(inches_to_cm(float(input())))
    elif a == 2:
        print(cm_to_inches(float(input())))
    elif a == 3:
        print(ml_to_km(float(input())))
    elif a == 4:
        print(km_to_ml(float(input())))
    elif a == 5:
        print(pound_to_kg(float(input())))
    elif a == 6:
        print(kg_to_pound(float(input())))
    elif a == 7:
        print(ounce_to_gr(float(input())))
    elif a == 8:
        print(gr_to_ounce(float(input())))
    elif a == 9:
        print(gl_to_ltr(float(input())))
    elif a == 10:
        print(ltr_to_gl(float(input())))
    elif a == 11:
        print(pint_to_ltr(float(input())))
    elif a == 12:
        print(ltr_to_pint(float(input())))
