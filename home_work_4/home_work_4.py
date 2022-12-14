# Парадокс Монти Холла — одна из известных задач теории вероятностей, решение которой, на первый взгляд,
# противоречит здравому смыслу. Парадокс основан на американском телешоу «Let's Make a Deal» и назван в
# честь ведущего этой передачи.
# Правила игры
# Участнику игры нужно выбрать одну из трёх дверей. За одной из дверей находится приз, за двумя другими
# дверями ничего нет. Участник выбирает одну из дверей, например, номер 1, после этого ведущий, который
# знает, где находится приз, открывает одну из оставшихся дверей, например, номер 3, за которой ничего нет.
# После этого он спрашивает участника, не желает ли он изменить свой выбор и выбрать дверь номер 2?
# Участник может согласиться либо остаться при своём выборе.
# Вопрос
# Увеличиваются ли шансы участника выиграть приз, если он примет предложение ведущего и изменит свой
# выбор?
# Предположения:
#  Математики утверждают, что увеличатся на 60%.
#  Разум подсказывает, что нет.
#
# Напишите программу, которая подтвердит или опровергнет доводы математиков. Чтобы это выполнить
# напишите функцию которая принимает два параметра: номер двери, которую открываем при первом вопросе,
# и переменную булевого типа, которая означает, меняет ли человек свой выбор при второй попытке открытия
# двери. Функция должна возвращать переменную булевого типа, которая означает, выиграл человек или
# проиграл. Запустите функцию в цикле > 1000 раз и подсчитайте соотношение выигрышей к проигрышу при
# смене двери и при отказе от смены двери.

from random import randrange


def win_loos(door, change):
    choice_door = randrange(1, 4)
    if door == choice_door:
        if change:
            return False
        else:
            return True
    else:
        if change:
            return True
        else:
            return False


games = 10000
win = 0
change = True
for j in range(2):
    for i in range(games):
        door = randrange(1, 4)
        if win_loos(door, change):
            win += 1
    print(f'Изменение выбора: {change}, результат: {round(win / games * 100, 2)} %')
    change = False
    win = 0
