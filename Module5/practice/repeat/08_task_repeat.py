def simple_percent(v, p, n):
    return round(v*(1+p*n/100), 2)

def hard_percent(v, p, n):
    return round(v*(1+p/100/12)**(12*n), 2)


def lucky_percent(money, first_pc, second_pc, deposit_age):
    if simple_percent(money, first_pc, deposit_age) < hard_percent(money, second_pc, deposit_age):
        return "сложные"
    else:
        return "простые"


print(f" Выгоднее вклад использующий {lucky_percent(100, 8, 6, 8)} проценты")
