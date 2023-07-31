def true_palindrom():
    s = input('Введите проверяемую строку без пробелов: ')
    print('Пример входных данных:\n ', s.lower())
    print('Пример выходных данных:\n ', str(s.lower()) == str(s[::-1].lower()))


true_palindrom()
