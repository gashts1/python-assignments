vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# this is the less intellignet way to do the task lol
# o = open('output/veggies.csv', 'w')
# o.write('name, color, name length \n')
#
# for veggie in vegetables:
#     o.write(veggie["name"])
#     o.write(', ')
#     o.write(veggie["color"])
#     o.write(', ')
#     o.write(str(len(veggie["name"])))
#     o.write('\n')

import csv

o = open('output/veggies2.csv', 'w')
writer = csv.writer(o)
writer.writerow(["name", "color", "length"])

for veggie in vegetables:
    writer.writerow([veggie["name"], veggie["color"], str(len(veggie["name"]))])

o.close()
