products = [5401, 7120, 8315, 1022, 9156, 4468]

search_products=int(input('What product are you looking for: '))

found = False

for product in products:
    if product == search_products:
        found = True
        break

if found:
    print('product found')

else:
    print('product not found')

