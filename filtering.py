import csv

with open('output/veggies2.csv', 'r') as f:
    vegetables = csv.DictReader(f)
    rows = list(vegetables)
    print(rows)
