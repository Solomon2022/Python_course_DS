# Реализуйте проверку ввода на число.
# Программа должна выводить “Correct”, если введено целое или вещественное число (в качестве разделителя
# должна использоваться одна точка).
# Во всех остальных случаях должно выводиться “Wrong”.

number = input('Введите число: ')

if number.isdigit():
    print('Correct')
else:
    try:
        number = float(number)
        print('Correct')
    except:
        print('Wrong')