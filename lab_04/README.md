# Прог. Лабораторная работа №1
###   Знакомство
## 00_distance
### Дан словарь с координатами городов. При помощи формулы - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, нужно посчитать растояние между городами.
### КОД:
```python
     sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distance = {
    'Moscow=>London' : (((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5),
    'London=>Paris' : (((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5),
    'Paris=>Moscow' : (((480 - 550) ** 2 + (480 - 370) ** 2) ** 0.5),
}
print(distance)
````

### РЕЗУЛЬТАТ:
![00.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/00.png)
## 01_circle
### Дан радиус круга: r= 42 и пи = 3.1415926.  Нужно найти пложнадь круга до точности в 4 знака после запятой. Точность мы указываем при помощи round().
### Так же даны 2 точки point_1 = (23, 34) и point_2 = (30, 30), надо определить, лежат они внутри круга или нет.
### КОД:
```python
radius = 42
point_1 = (23, 34)
point_2 = (30, 30)
S = radius**2 * 3.1415926
S = round(S,4)
M = point_1 = (23**2 + 34**2)**0.5
print("S = ", S)
if M < radius:
    print("Точка M находится внутри кругa")
else:
    print("Точка М не находится внутри круга")
N = (30**2 + 30**2) ** 0.5
if N < radius:
    print("Точка N находится внутри кругa")
else:
    print("Точка N не находится внутри круга")
```
### РЕЗУЛЬТАТ:
![01.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/01.png)
## 02_operation
### Надо между числа '1 2 3 4 5' раставить знаки операций так, что бы получился ответ 25.
### КОД:
```python
result = 1 * ((2 + 3) + (4 * 5))
print(result)
```
### РЕЗУЛЬТАТ:
![02.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/02.png)
## 03_favorite_movies
### Надо при помощи индексации вывести на консоль фильмы из списка:
### my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее' 
### в порядке - первый фильм, последний, второй, второй  с конца
### КОД:
```python
a = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(a[0:10],',', a[-15:-1],',', a[12:25],',', a[-22:-17])
```
### РЕЗУЛЬТАТ:
![03.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/03.png)
## 04_my_family
### Создаём список my_family = [] состоящий минимум из трёх элементов.
### При помощи данного списка заполняем список my_family_height = [] и добавляе рост каждому элементу списка
### Выводим на консоль отдельно рост отца, и общий рост всех членов семьи.
### КОД:
```python
my_family = ["Илья", "Сергей", "Оксана"]
my_family_height = [my_family[0],194,my_family[1],186,my_family[2],182]
a = my_family_height[1]+my_family_height[3]+my_family_height[5]
print("рост отца -" ,my_family_height[3],"cm")
print(a, "- сумма ростов членов семьи")
```
### РЕЗУЛЬТАТ:
![04.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/04.png)
## 05_zoo
### Дан список животных zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ].
### Нужно посадить между 'lion' и 'kangaroo' 'bear', и вывести список.
###  Дальше надо обьединить список birds = ['rooster', 'ostrich', 'lark', ] с списком zoo и вывести в консоль.
### Убираем слона и снова выводим список в консоль.
### Выводим на консоль клетки, в который сидит 'lion' и 'lark'.
### КОД:
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]
zoo.insert(1,'bear')
zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])
zoo.pop(3)
print(zoo)
print("лев в клетке", zoo.index('lion')+1, ",", "жаворонок в клетке",zoo.index('lark')+1)
```
### РЕЗУЛЬТАТ:
![05.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/05.png)
## 06_song_list
### Дан список песен Depeche Mode со временем звучания с точностью до долей минут.
### Нужно вывести на консоль общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'
### в формате: Три песни звучат ХХХ.XX минут
### Так же дан словарь песен Depeche Mode, надо вывести общее время звучания трех песен:
### 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress' в формате:  А другие три песни звучат ХХХ минут.
### КОД:
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
a=violator_songs_list[3][1]
b=violator_songs_list[5][1]
c=violator_songs_list[8][1]
time0 = a + b + c
time0 = round(time0,2)

print('три песни звучат', time0, 'минут')
n = violator_songs_dict['Sweetest Perfection']
m = violator_songs_dict['Policy of Truth']
r = violator_songs_dict['Blue Dress']
time1 = n + m + r
time1 =round(time1,1)
print("а другие три песни звучат", time1, "минут")
```
### РЕЗУЛЬТАТ:
![06.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/06.png)
## 07_secret
### Есть зашифрованное сообщение
### secret_message = [
###    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
###    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
###    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
###    'ьд5фму3ежородт9г686буиимыкучшсал',
###    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
### ]
### с помощью индексации расшифровываем и при поддержке ключей расшифровываем сообщение
+ ### Ключи к расшифровке:
1. ###   первое слово - 4-я буква
2. ###   второе слово - буквы с 10 по 13, включительно
3. ###   третье слово - буквы с 6 по 15, включительно, через одну
4. ###   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
5. ###   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
### КОД:
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
a = secret_message[0][3]
b = secret_message[1][9:13]
c = secret_message[2][5:15:2]
d = secret_message[3][12:6:-1]
e = secret_message[4][20:15:-1]
secret = a + ' ' + b + ' ' + c + ' ' + d + ' ' + e
print(secret)
```
### РЕЗУЛЬТАТ:
![07.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/07.png)
## 08_garden
### Даны кортежи garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
### и meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
- ### Задачи:
1. #### При помощи set() переделываемм их в списки.
2. #### выводим на консоль все виды цветов.
3. #### выводим на консоль те, которые растут и там и там.
4. #### выводим на консоль те, которые растут в саду, но не растут на лугу.
5. #### выводим на консоль те, которые растут на лугу, но не растут в саду.
### КОД:
```python
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = set(garden)
meadow_set = set(meadow)
allflowers = garden + meadow
allflowers_set = set(allflowers)
print(allflowers_set,  "все  цветы")
print(garden_set, "цветы растущие в саду")
print(meadow_set, "цветы растущие на лугу")
print(garden_set-meadow_set, "цветы растущие только в саду")
print(meadow_set-garden_set, "цветы растущие только на лугу")
```
### РЕЗУЛЬТАТ:
![08.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/08.png)
## 09_shoping
### Дан словарь магазинов shops в который входят ашан, пятёрочка и магнит, а так же сладости.
### Надо создать словарь цен, состоящий из двух магазинов с минимальными ценами.
### КОД:
```python
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99}
    ],
    'конфеты': [
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ],
}
print(sweets.setdefault('печенье'))
print(sweets.setdefault('конфеты'))
print(sweets.setdefault('карамель'))
print(sweets.setdefault('пирожное'))
```
### РЕЗУЛЬТАТ:
![09.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/09.png)
## 10_store
### Есть словарь кодов товаров - goods = {} и словарь списков количества товара на складе store = {}
### Рассчитать на какую сумму лежит каждого товара на складе
### КОД:
```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
table_code = goods['Стол']
tables_item = store[table_code][0]
tables_item1 = store[table_code][1]
tables_quantity = tables_item['quantity']
tables_quantity1 = tables_item1['quantity']
tables_price = tables_item['price']
tables_price1 = tables_item1['price']
tables_cost = tables_quantity * tables_price
tables_cost1 = tables_quantity1 * tables_price1
print('Стол -', tables_quantity+tables_quantity1, 'шт, стоимость', tables_cost+tables_cost1, 'руб')

sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_item1 = store[sofa_code][1]
price1 = sofas_item['quantity']* sofas_item['price']
price2 = sofas_item1['quantity']* sofas_item1['price']
sofa_cost = price1 + price2
sofas_quantity = sofas_item['quantity']+sofas_item1['quantity']

print('Диван -', sofas_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_item1 = store[chair_code][1]
chair_item2 = store[chair_code][2]
chair_cost = chair_item['quantity'] * chair_item['price'] + chair_item1['quantity'] * chair_item1['price'] + chair_item2['quantity'] * chair_item2['price']
chair_quantity = chair_item['quantity'] + chair_item1['quantity'] + chair_item2['quantity']
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')

```
### РЕЗУЛЬТАТ:
![10.png](https://github.com/MbSmD/programming/blob/main/lab_04/screenshots/10.png)



