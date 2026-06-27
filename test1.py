book_ids = [2045, 1789, 3467, 4123, 2891, 1560, 3894]

search_id = int(input('Which book are you looking for: '))

found = False

for book in book_ids:
    if book == search_id:
        found = True
        break

if found:
    print('book available')

else:
    print('book not available')