import json

filename = 'favourite_number.json'

with open(filename) as f:
    your_fav_number = json.load(f)


print(f"I know your favourite number, it's {your_fav_number}.")
