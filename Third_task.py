# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


a = [2, 2, 3, 4, 5, 1, 5, 5, 3, 8, 9]
print(f'Исходный список: {a}')
new_list = []
for i in a:
     if a.count(i) == 1:
         new_list.append(i)
print(f'Значения, которые встречаются в исходном списка один раз: {new_list}')


