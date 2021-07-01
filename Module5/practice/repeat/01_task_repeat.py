# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    li = []
    for _ in range(size):
        li.append(random.randint(of, to))
    return li


l = gen_list(5, 1, 100)

print(l)
