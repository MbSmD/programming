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

