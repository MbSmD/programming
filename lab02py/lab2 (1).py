from itertools import product

# Задача 1
letters = ['В', 'И', 'Ш', 'Н', 'Я']
vowels = ['И', 'Я']
count = 0

for word in product(letters, repeat=6):
    word_str = ''.join(word)
    if word_str[0] == 'Ш':
        continue
    if word_str[-1] in vowels:
        continue
    if word_str.count('В') > 1:
        continue
    valid_words_count += 1

print("Количество подходящих слов:", count)

# Задача 2
result = 4 * (2014 + 2 * 2015 - 8)
binary_representation = bin(result)
ones_count = binary_representation.count('1')
print("Количество единиц в двоичной записи:", ones_count)

# Задача 3
lbound = 400_000_000
ubound = 600_000_000
valid_numbers = []

for m in range(0, 30):
    if m % 2 != 0:
        continue
    for n in range(1, 20):
        if n % 2 == 0:
            continue
        N = (2 ** m) * (3 ** n)
        if lbound <= N <= ubound:
            valid_numbers.append(N)

print("Найденные числа:", sorted(valid_numbers))
