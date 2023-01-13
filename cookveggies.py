import json
import csv

with open('output/veggies2.csv', 'r') as f:
    vegetables = csv.DictReader(f)
    rows = list(vegetables)
    print(rows)

with open('output/vegetables.json', 'w') as f:
    json.dump(rows, f, indent=2)
