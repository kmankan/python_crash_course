import json
filename = 'favourite_number.json'


def favourite_number():
    """Check to see if favourite number json file already exists, if it does
    print that number. If not, ask the user for their favourite number
    and store it as a json file."""
    try:
        with open(filename) as f:
            your_fav_number = json.load(f)
            print(f"I know your favourite number, it's {your_fav_number}.")
    except FileNotFoundError:
        your_fav_number = input("What is your favourite number? ")
        with open(filename, 'w') as f:
            json.dump(your_fav_number, f)
            print("Your number has been stored")


favourite_number()






