from itertools import product

# Задача 1
letters = ['В', 'И', 'Ш', 'Н', 'Я']
vowels = ['И', 'Я']
valid_words_count = 0

for word in product(letters, repeat=6):
    word_str = ''.join(word)
    if word_str[0] == 'Ш':
        continue
    if word_str[-1] in vowels:
        continue
    if word_str.count('В') > 1:
        continue
    valid_words_count += 1

print("Количество подходящих слов:", valid_words_count)

# Задача 2
result = 4 * (2014 + 2 * 2015 - 8)
binary_representation = bin(result)
ones_count = binary_representation.count('1')
print("Количество единиц в двоичной записи:", ones_count)

# Задача 3
lower_bound = 400_000_000
upper_bound = 600_000_000
valid_numbers = []

for m in range(0, 30):
    if m % 2 != 0:
        continue
    for n in range(1, 20):
        if n % 2 == 0:
            continue
        N = (2 ** m) * (3 ** n)
        if lower_bound <= N <= upper_bound:
            valid_numbers.append(N)

print("Найденные числа:", sorted(valid_numbers))
