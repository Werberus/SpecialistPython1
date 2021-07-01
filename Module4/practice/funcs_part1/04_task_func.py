def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


def can_triangle(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    if (a + b > c) & (a + c > b) & (b + c > a):
        return True
    return False


# Пример вызова функции
print(can_triangle((14, 18), (14, 18), (12, 12)))
