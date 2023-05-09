def lab21():
    k1 = input("Введите пароль ")

    if len(k1) < 5:
        print("Пароль слишком короткий")
    else:
        k2 = input("Введите еще раз, чтобы подтвердить ")
        if k2 != k1:
            print("Неверно. Попробуйте снова")
        else:
            print("Пароль подвержден")


print(lab21())


def lab22():
    n = int(input("Номер? "))

    if n % 2 == 0 and n in range(1, 37):
        print("Верх")
    if n % 2 != 0 and n in range(1, 37):
        print("Низ")

    if n % 2 == 0 and n in range(37, 55):
        print("вверх боковушки")
    if n % 2 != 0 and n in range(37, 55):
        print("Низ боковушки")

    if n > 54:
        print("Неправильный номер")


print(lab22())


def lab23():
    y = int(input("Введите номер года"))
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Год", y, " - високосный")
    else:
        print("год не високосный")


print(lab23())


def lab24():
    c1 = input("1 цвет")
    c2 = input("2 цвет")

    q = "желтый"
    w = "красный"
    e = "синий"

    if (c1 == w or c2 == w) and (c1 == e or c2 == e):
        print("фиолетовый")
    if (c1 == w or c2 == w) and (c1 == q or c2 == q):
        print("оранжевый")
    if (c1 == e or c2 == e) and (c1 == q or c2 == q):
        print("зеленый")


print(lab24())


def lab25():
    n = int(input("сколько слов?"))
    s = ''
    for i in range(n):
        a = input()
        s += a + ' '
    print(s)


print(lab25())
def lab31():
    n = int(input("Сколько слов?"))
    s = ''
    for i in range(n):
        a = input()
        s += a + ' '
    print(s)


print(lab31())


def lab32():
    a = input()
    s = ''
    while a != "stop":
        s += a + " "
        a = input()
    print(s)


print(lab32())


def lab33():
    a = input()
    while a != 'stop':
        if 'ф' in a or 'Ф' in a:
            print("WOW! Это редкое слово!")
        else:
            print("это не очень редкое слово...")
        a = input()


print(lab33())


def lab34():
    import random
    n = 0
    x = 0
    while n < 3:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        ab = str(a) + ' + ' + str(b) + ' = '
        s = int(input(ab))
        if s == a + b:
            print("Правильно")
            x += 1
        else:
            print("Ответ неверный")
            n += 1
    print("Правильных ответов:", x)


print(lab34())
def lab41():
    if number % 3 == 0:
        return True
    else:
        return False


number = int(input("введите число: "))
if lab41():
    print("число делится на 3")
else:
    print("число не делится 3")
print(lab41())


def lab42():
    try:
        a = int(input())
        s = 100 / a
    except ValueError:
        print("this is не число")
    except ZeroDivisionError:
        print("нельзя на 0")
    else:
        print("равно", s)


print(lab42())


def lab43():
    s = input("впишите дату в виде 02.11.2022")
    if int(s[0]) * int(s[1]) == int(s[2][2:]):
        print("magic")
    else:
        print("not magic")


print(lab43())


def labb44():
    s = input("Билет:")
    if len(s) % 2 == 0:
        g = int(len(s) / 2)
        s1 = 0
        s2 = 0
        for i in range(g):
            s1 += int(s[i])


print(labb44())
def lab51():
    n = [7, 2, 9, 6, 11]
    if int(input()) in n:
        print("с праздником! число есть в списке")
    else:
        print("увы, такого числа нет")


print(lab51())


def lab52():
    n = [7, 1, 7, 5, 7]
    a = []
    for i in n:
        if n.count(i) > 1:
            a.append(i)
    print(set(a))


print(lab52())


def lab53():
    w = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    a = int(input("Сколько выходных на неделе вы хотите?"))
    print("Ваши выходные:", print(w[-a:]))
    print("Рабочие:", w[:len(w) - a])


print(lab53())
def lab61():
    c = {"Russia": "Moscow", "France": "Paris", "Italy": "Rome", "Germany": "Berlin", "Spain": "Madrid",
         "Ukraine": "Kiev"}
    print(c["Russia"])
    for i in sorted(c):
        print(i, '-', c[i])


print(lab61())


def lab622():
    alp = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    s = input("Введите слово")
    summ = 0

    for i in s:
        summ += alp[i]

    print(summ)


print(lab622())

