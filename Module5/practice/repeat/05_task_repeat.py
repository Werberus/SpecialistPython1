# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def last_pagination(num_items, items_on_page):
    return num_items-(num_items//items_on_page*items_on_page)

print(last_pagination(21,4))
