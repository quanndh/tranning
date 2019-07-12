shop = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}

price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000
}

for key in shop:
    print(key, shop[key])

print(shop['MACBOOK'])

shop['TOSHIBA'] = 10

print(shop)

print("Don hang 5 ASUS:", price['ASUS'] * 5)