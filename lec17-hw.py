# dictionary question
dict_israel_details: dict = {
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
dict_copy: dict[str, str | list[str] | int | float] = dict_israel_details.copy()
print(dict_copy.pop("gdp_billions"))
print(dict_copy)

other_country_dict = dict_israel_details.fromkeys(dict_israel_details.keys())
other_country_dict["name"] = input("enter country name:")
other_country_dict["birth"] = int(input("enter birth year:"))
other_country_dict["population_millions"] = int(input("enter population number (millions):"))
other_country_dict["capital"] = input("enter capital name:")
other_country_dict["language"] = input("enter language name:")
other_country_dict["cities"] = [input("enter city name:") in range(3)]
other_country_dict["currency"] = input("enter currency name:")
other_country_dict["area_Kilometers"] = int(input("enter area number (Kilometers):"))
other_country_dict["gdp_billions"] = int(input("enter gdp number (Billions):"))
print(other_country_dict)


# leetcode question:
def lengthOfLastWord(s: str = "") -> int:
    s_list_last: list[str] = s.strip().split()
    return len(s_list_last[len(s_list_last) - 1])


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("luffy is still joyboy"))
