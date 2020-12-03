list_of_cases = ['Сделать дз', 'Сходить погулять']
#                     0                 1
list_of_cases.append('Заняться спортом')
#                             3
list_of_cases.append('Накормить собаку')
#                             4
list_of_cases.append('Стать лучшим в мире:)')
#                             5
list_of_cases.insert(2, 'Посидеть за компом')
#                             2
list_of_cases.pop(4)

print(list_of_cases)

print("Index for Стать лучшим в мире:)", list_of_cases.index('Стать лучшим в мире:)'))
print("Count for Стать лучшим в мире:)", list_of_cases.count('Стать лучшим в мире:)'))
