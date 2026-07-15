# names = ['rishat', 'shagor', 'Itvaya']

# for i in names:
#     print(i)
    
names = {
    'rishat' : 32,
    'shagor' : 69,
    'itvaya' : 420
}

for i in names:
    print(names[i])
    
    
fav_lang = {
    'rishat' : 'python',
    'shagor' : 'c++',
    'itvaya' : 'kotlin'
}

for i in fav_lang.keys():
    print(f"{i.title()} loves, {fav_lang[i].title()}")
    
print(fav_lang.values())
print(fav_lang.items())

for key, val in fav_lang.items():
    print(f"{key.title()} likes, {val.title()}")
    
    
# dummy_tuple = (10,13)

# x, y, z = (50,75, 832)

# print(x, y, z)
