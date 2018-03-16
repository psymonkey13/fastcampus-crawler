import json

dict_object = {
    'name': 'Junhum',
    'Nicname': 'Beomi',
    '메일주소': 'test@email.com'
}

json.dump(dict_object, open('sample.json', 'w'))

dict_object2 = json.load(open('sample.json'))
print(dict_object2)

