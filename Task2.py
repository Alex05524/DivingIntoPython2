# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

def to_hex(number):
    hex_string = hex(number)[2:]
    return hex_string.upper()

# Пример использования:
input_number = int(input("Введите целое число: "))
hexadecimal = to_hex(input_number)
print("Шестнадцатеричное представление:", hexadecimal)

# Проверка результата с использованием функции hex()
hex_check = hex(input_number)[2:].upper()
print("Проверка с помощью hex():", hex_check)