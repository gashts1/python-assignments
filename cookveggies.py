
import csv
import json


#3.3

# 1 reading created vegetables csv file
with open('output/vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#2 Print the variable vegetables.
print(vegetables)


#3 Write vegetables as a JSON file called output/vegetables.json. 
with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f)


#.........................
#1 Reads superheroes.json (in this folder)

with open('superheroes.json', 'r') as f:
    data = json.load(f)
f.close()
#2 Creates an empty array called powers
powers=[]


#3 Loop thorough the members of the squad, and append the powers of each to the powers array.

members=data["members"]  
for items in range(0,len(members)):
    dic={}
    dic=members[items] 
    
    pow_loop=dic["powers"]
    powers.append(pow_loop)

#4 Prints those powers to the terminal
print(powers)

#Bonus: make the list of powers unique and print it again
print(powers) # did this in one go with #4


#...............................................

#1Read superheroes.json
with open("superheroes.json") as f:
    superheroes = json.load(f)

#2 Write a header to the CSV file
with open("superheroes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "name",
            "age",
            "secretIdentity",
            "powers",
            "squadName",
            "homeTown",
            "formed",
            "secretBase",
            "active",
        ]
    )
    for superhero in superheroes["members"]:
        writer.writerow(
            [
                superhero["name"],
                superhero["age"],
                superhero["secretIdentity"],
                superhero["powers"],
                superheroes["squadName"],
                superheroes["homeTown"],
                superheroes["formed"],
                superheroes["secretBase"],
                superheroes["active"],
            ]
        )


 #bonus 
 #writing one row per power than per member and storing in superheroes.json

with open("superheroes2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "name",
            "age",
            "secretIdentity",
            "powers",
            "squadName",
            "homeTown",
            "formed",
            "secretBase",
            "active",
        ]
    )
    for superhero in superheroes["members"]:
        for power in powers:
            writer.writerow(
            [
                superhero["name"],
                superhero["age"],
                superhero["secretIdentity"],
                superhero["powers"],
                superheroes["squadName"],
                superheroes["homeTown"],
                superheroes["formed"],
                superheroes["secretBase"],
                superheroes["active"],
            ]
        )



#1. Set a variable birthday = "1-May-12".

#2. Parse the date using datetime.datetime.strptime.
#3. Use strftime to output a date that looks like "5/1/2012".

from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y")  # 01/11/17
print(date_str)

birthday = "1-May-12"
parsted_birthday = datetime.strptime(birthday, "%d-%b-%y")
birthdate_str = parsted_birthday.strftime("%m/%d/%y")

print(birthdate_str)



#3.5..............................................

green_veggies = []

with open("output/vegetables.csv", "r") as f:
    reader = csv.DictReader(f)
    veggies = [row for row in reader]
    for row in veggies:
        if row["color"] == "green":
            green_veggies.append(row)

with open("output/greenveggies.json", "w") as f:
    json.dump(green_veggies, f)

with open("output/green_vegetables.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=green_veggies[0].keys())
    writer.writeheader()
    writer.writerows(green_veggies)