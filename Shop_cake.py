shop = {"Капкейк": [["мука","яйца","шоколад","молоко", "разрыхлитель"],3.5,1500],
              "Наполеон": [["сахар","яйца","сметана","мука", "сливочное масло"],4.0,2700],
              "Павлова": [["яичный белок", "сахар", "маскарпоне", "лесные ягоды"],5,1000]}
print('Здравствуйте. Для выбора введите:"состав", "цена", "количество", "общая информация"')
while True:
    a = input('Введите что вам подсказать: ')
    if a == "состав":
        for key,value in shop.items():
            print(key,'-',','.join(value[0]))
    if a == "цена":
        for key,value in shop.items():
            print(key,f'- {value[1]}р. за 100гр.')
    if a == "количество":
        for key,value in shop.items():
            print(key,f'- {value[2]} гр.')
    if a == "общая информация":
        for key,value in shop.items():
            print(f'\n {key}', '\nСостав:', ",".join(value[0]),
                  f'\nЦена: {value[1]}р. за 100гр.', f'\nКоличество: {value[2]} гр.')
    else:
        cost = 0
        while True:
            good = input('Что вы хотите купить? "Капкейк", "Наполеон", "Павлова" или '
                             'введите n для завершения покупок')
            if good == 'n':
                break
            gram = int(input('Сколько грамм вы хотите купить?'))
            if gram>shop[good][2]:
                print("У нас столько нет, выберите другое количество или товар")
                continue
            cost = cost + (gram/100 * shop[good][1])
            shop[good][2] -= gram
        print(f"Вам надо заплатить {cost} р.")
    for key, value in shop.items():
        print(f'\n{key}', f'\nОсталось {value[2]} гр.')
    print("До свидания")






# print(len(set(input().split()).intersection(set(input().split()))))
#
# with open("plan.txt") as file:
#     a_sum = a_count = 0
#     for line in file.readlines():
#         line = line.rstrip("\n")
#         a_count += 1
#         a = int(line[-1])
#         a_sum += a
#         if a < 3:
#             print("Студент, чья оценка меньше 3-х:", line[:-1])
# print("Средний бал по группе:", a_sum / a_count)











