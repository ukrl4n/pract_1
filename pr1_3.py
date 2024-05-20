import numpy as np


# Функція для створення матриці обертання
def rotation_matrix(theta):
    # Перетворюємо градуси в радіани
    theta = np.radians(theta)
    # Створюємо матрицю обертання за допомогою формул обертання
    return np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])


# Функція для створення матриці масштабування
def scaling_matrix(sx, sy):
    # Створюємо матрицю масштабування, використовуючи задані коефіцієнти масштабування
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])


# Функція для створення матриці переміщення
def translation_matrix(tx, ty):
    # Створюємо матрицю переміщення, використовуючи задані коефіцієнти переміщення
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])


# Головна функція для виконання послідовності трансформацій
def modelMatrix(inMatrix, sequence):
    # Створюємо словник функцій для кожної трансформації
    operations = {'R': rotation_matrix, 'S': scaling_matrix, 'T': translation_matrix}

    # Визначаємо вихідний вектор
    vector = np.array([*inMatrix['V'], 1])

    # Застосовуємо трансформації в заданому порядку
    for operation in sequence:
        # Використовуємо матричне множення для застосування трансформації до вектора
        vector = np.dot(operations[operation](*inMatrix[operation]), vector)

    # Повертаємо результуючий вектор, відкидаючи останній елемент
    return vector[:-1]


# Тестовий блок
inMatrix = {'R': (15.0,), 'T': (2.0, 2.0), 'S': (1.5, 2.7), 'V': (6, 2)}
result = modelMatrix(inMatrix, 'SRT')
print(f"Після застосування трансформацій {inMatrix} в порядку 'SRT', вектор перетворюється в {result}")

inMatrix = {'R': (51.0,), 'T': (3.0, 2.0), 'S': (1.0, 3.2), 'V': (6, 2)}
result = modelMatrix(inMatrix, 'TRS')
print(f"Після застосування трансформацій {inMatrix} в порядку 'TRS', вектор перетворюється в {result}")