# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]

print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

max_sal = 0
max_name = ""
for a in staff:
    if a.get("salary") > max_sal:
        max_sal = a.get("salary")
        max_name = a.get("name")
print(max_name,"\n")


print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

min_sal = max_sal
min_name = ""
for a in staff:
    if a.get("salary") < min_sal:
        min_sal = a.get("salary")
        min_name = a.get("name")
print(min_name,"\n")

print("Среднеарифметическую зарплату всех сотрудников")

sal = 0
for a in staff:
    sal += a.get("salary")
print(round(sal/len(staff), 2),"\n")

print("Количество однофамильцев в организации")

namer = 0
for a in staff:
    for b in staff:
        if a != b:
            if a.get("surname") == b.get("surname"):
                namer +=1
                break
print(namer, "\n")


print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")


for a in range(len(staff)):
    i = 0
    while i < len(staff)-1:
        if staff[i].get("salary") > staff[i+1].get("salary"):
            staff[i], staff[i+1] = staff[i+1], staff[i]
        i += 1

for a in staff:
    print(f"{a.get('name')}, {a.get('surname')}, {a.get('salary')}")
