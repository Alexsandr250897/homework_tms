import  json
with open("city.list.json") as file:
    data = json.load(file)

    dict_city = {}
    for i in data:
        if i["country"] not in dict_city:
            dict_city[i["country"]] = 0
        else:
            dict_city[i["country"]] += 1


    northern_city = {}
    southern_city = {}
    count = 0
    for i in data:
        if 0 < i["coord"]["lat"] :
            northern_city[i["coord"]["lat"]]=0
        else:
            0 > i["coord"]["lat"]
            southern_city[i["coord"]["lat"]]=1

print(f"Колличество городов : {len(northern_city) + len(southern_city)}")

print(f"Колличество северных городов : {len(northern_city)}  "
        f"Колличество южных городов :  {len(southern_city)} ")
print(f"Код страны и колличество городов : {dict_city}")

