dict_israel_details = {
    "name": "Israel",
    "birth": 1984,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Reshion LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_Kilometers": 22_145,
    "gdp_billions": 450
}
print("capital:", dict_israel_details.get("capital"))
print("keys", list(dict_israel_details.keys()))
print("values", list(dict_israel_details.values()))
for key, value in dict_israel_details.items():
    print(f"{key}:{value}")
dict_copy:dict[str, str | list[str] | int | float] = dict_israel_details.copy()
print(dict_copy.pop("gdp_billions"))
print(dict_copy)
empty_dic = dict_israel_details.fromkeys(dict_israel_details.keys())
empty_dic["name"] = input("enter country name:")
empty_dic["birth"] = int(input("enter birth year:"))
empty_dic["population_millions"] = int(input("enter population number (millions):"))
empty_dic["capital"] = input("enter capital name:")
empty_dic["language"] = input("enter language name:")
empty_dic["cities"] = [input("enter city name:") in range(3)]
empty_dic["currency"] = input("enter currency name:")
empty_dic["area_Kilometers"] = int(input("enter area number (Kilometers):"))
empty_dic["gdp_billions"] = int(input("enter gdp number (Billions):"))
print(empty_dic)
