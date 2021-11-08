people=[ {"name": "Harry", "house": "Ravenclaw"},
{"name": "Valli", "house": "ValliHouse"},
{"name": "Ananya", "house": "AnanyaHouse"},
{"name": "Broc", "house": "Brookside"}]

#sort using fuction
# def f(person):
#   return person["name"]

#people.sort(key=f)


#using lambda function
people.sort(key= lambda person: person["name"])

print(people)