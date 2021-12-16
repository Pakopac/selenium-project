import csv
import sys

with open('datas/characters.csv', 'r') as csvfile:
    characters = csv.reader(csvfile)
    characters = list(characters)
    damage = characters[int(sys.argv[1])][1]
    tears = characters[int(sys.argv[1])][2]
    statRange = characters[int(sys.argv[1])][3]
    print(f"--- {characters[int(sys.argv[1])][0]} ---")

with open('datas/items.csv', 'r') as csvfile:
    items = csv.reader(csvfile)
    items = list(items)
    for i in range(len(sys.argv)):
        if i > 1:
            damage = float(damage) + float(items[int(sys.argv[i])][1])
            tears = float(tears) + float(items[int(sys.argv[i])][2])
            statRange = float(statRange) + float(items[int(sys.argv[i])][3])
    print(f"Damage: {damage}")
    print(f"Tears: {tears}")
    print(f"Range: {statRange}")

