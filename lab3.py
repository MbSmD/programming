def split(lst, n):
    # Создаем список для хранения n частей
    result = [[] for _ in range(n)]
    
    # Распределяем элементы по частям
    for i, item in enumerate(lst):
        result[i % n].append(item)
    
    return result

def calculate_v(n):
    # Инициализируем список значений
    v = [0] * max(n + 1, 4)  # Убедимся, что список достаточно велик
    v[1] = 0
    v[2] = 0
    v[3] = 1.5

    # Вычисляем значения v_i по формуле
    for i in range(4, n + 1):
        v[i] = (i ** 2 + 1) / (i + 1) * v[i - 1] - v[i - 2] * v[i - 3]

    return v[1:n + 1]

# Примеры использования
print(split([1, 2, 3, 4, 5], 2))  # [[1, 3, 5], [2, 4]]
print(split([1, 2, 3, 4, 5], 3))  # [[1, 4], [2, 5], [3]]
print(calculate_v(5))  # [0, 0, 1.5, ...]
