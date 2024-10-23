# TODO Найдите количество книг, которое можно разместить на дискете
symbols = 25
lines = 50
pages = 100
for_one_symbols = 4
Volum_disk = (1.44*1024*1024)
one_book = int(pages*lines*symbols*for_one_symbols)
number_of_books = int((Volum_disk//one_book))
print("Количество книг, помещающихся на дискету:", number_of_books)
