cats = 'cats.txt'
dogs = 'dogs.txt'

print("Let's name three cats!")
try:
    with open(cats) as f1:
        print(f1.read())
except FileNotFoundError:
    #print(f"The file named {cats} could not be found.")
    # fail silently
    pass

print("\nLet's name three dogs!")
try:
    with open(dogs) as f2:
        print(f2.read())
except FileNotFoundError:
    #print(f"The file named {dogs} could not be found.")
    # fail silently
    pass
