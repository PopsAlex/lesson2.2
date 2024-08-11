try:
    first = int(input('Введите первое число (целое): '))
    second = int(input('Введите первое целое число (тоже целое): '))
    third = int(input('Введите первое целое число (всё ещё целое): '))

    if first == second == third:
        print('3')
    elif first == second or first == third or second == third:
        print('2')
    elif first != second and first != third and second != third:
        print('0')

except ValueError:
    print('А Вы шутник')


