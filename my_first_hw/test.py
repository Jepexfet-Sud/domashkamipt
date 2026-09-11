s='просо колесо мясо лассо серсо'
vows = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
cons = ['б', 'в', 'г', 'д', 'ж', 'з','й', 'к', 'л', 'м', 'н', 'п','р', 'с', 'т', 'ф', 'х', 'ц','ч', 'ш', 'щ', 'ъ', 'ь']
r=""
for i, char in enumerate(s):
    if i == 0 and char in vows and len(s) == 1:
        r += char + 'с' + char
    elif i == 0 and char in vows and s[1] not in vows:
        r += char + 'с' + char
    elif i != 0 and char in vows and s[i-1] in cons:
        r += char + 'с' + char
    else:
        r += char
print(r)