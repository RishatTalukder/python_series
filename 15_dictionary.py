# cat = ['green', 18, 3, 'bhau bhau']

# cat = {"color": 'green', 'age': 18}

cat = {
    'color': 'brown',
    'age': 18
}

print(cat)

print(cat['color'])
print(cat['age'])

cat['eye color'] = 'red'

print(cat)

cat['color'] = 'orange'

print(cat)

del cat['color']

print(cat)

print(cat.get('color', 'no color'))