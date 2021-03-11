import os

file_path = os.path.join(os.getcwd(), 'cook_book.txt')
cook_book = {}
with open(file_path, "r", encoding="utf-8") as f:
    try:
        while True:
            ingredient = f.readline().rstrip()
            cook_book[ingredient] = []
            cnt_ingredients = int(f.readline().rstrip())
            for j in range(cnt_ingredients):
                lst = f.readline().rstrip().split(' | ')
                cook_book[ingredient].append({'ingredient_name': lst[0], 'quantity': int(lst[1]), 'measure': lst[2]})
            print(f.readline().rstrip(), end='')
    except ValueError:
        del cook_book['']
print(cook_book)

