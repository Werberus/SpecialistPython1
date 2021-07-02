# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего
with open("data/limericks.txt", "r", encoding="utf-8") as file:
    count_char = 0
    count_bit = 1
    for f in file:
        print(f.rstrip())
        count_char += len(f.rstrip().replace(" ", ""))
        if f.rstrip() == "":
            count_bit += 1
    print("\nколичество символов:", count_char)
    print("количество стихотворений:", count_bit)
