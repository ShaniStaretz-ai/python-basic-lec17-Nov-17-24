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
other_country_dict["name"] = input("enter country name:").capitalize()
other_country_dict["birth"] = int(input("enter birth year:"))
other_country_dict["population_millions"] = float(input("enter population number (millions):"))
other_country_dict["capital"] = input("enter capital name:").capitalize()
other_country_dict["language"] = input("enter language name:").capitalize()
other_country_dict["cities"] = [input("enter city name:").capitalize() for _ in range(3)]
other_country_dict["currency"] = input("enter currency name:").upper()
other_country_dict["area_Kilometers"] = int(input("enter area number (Kilometers):"))
other_country_dict["gdp_billions"] = int(input("enter gdp number (Billions):"))
print(other_country_dict)


# leetcode question:
def lengthOfLastWord(s: str = "") -> int:
    s_list_last: list[str] = s.strip().split()
    return len(s_list_last[len(s_list_last) - 1])


print("length Of Last Word of 'Hello World'",lengthOfLastWord("Hello World"))
print("length Of Last Word of '   fly me   to   the moon  ':",lengthOfLastWord("   fly me   to   the moon  "))
print("length Of Last Word of 'luffy is still joyboy':",lengthOfLastWord("luffy is still joyboy"))
