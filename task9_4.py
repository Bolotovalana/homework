# 4. Написатьпрограмму,котораяищетчисла,делящиесяна19или13в списке чисел , используя lambda функцию.
# Пример:
# На вход дается список: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] На выход числа из приведенного выше
# списка, кратные 19 или 30: [19, 65, 57, 39, 152, 190]

list1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(list(filter(lambda x: x % 30 == 0 or x % 19 == 0, list1)))