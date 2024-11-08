# TODO Напишите функцию для поиска индекса товара

def first_inclusion(items_list, item_to_find):
    for i in range(len(items_list)):
        if item_to_find == items_list[i]:
            return i


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = first_inclusion(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
