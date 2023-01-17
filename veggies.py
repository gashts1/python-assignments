import csv
# 1 Write a python script called veggies.py that defines a list of dicts named vegetables like so:

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


# 2 In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv
with open('output/vegetables.csv', 'w') as g:
    writer = csv.writer(g)

    writer.writerow(["name", "color"])

    for veggie in vegetables:
        print(writer.writerow([veggie["name"], veggie["color"]]))


# reading created vegetables csv file
with open('output/vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)



#3 Bonus

with open('output/vegetables.csv', 'w') as o:
    writer = csv.writer(o)
    writer.writerow(["name", "color", "length"])

    for veggie in vegetables:
        writer.writerow([veggie["name"], veggie["color"], str(len(veggie["name"]))])