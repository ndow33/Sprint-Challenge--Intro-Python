import csv
from cityreader import City


# read the file
out = open('cities.csv', 'r')
data = csv.reader(out)
data = [row for row in data]
out.close()

# transfer data into a city objects and store in a list
cities = []
for x in range(1,len(data)):
    new_city = City(data[x][0], float(data[x][3]), float(data[x][4]))
    cities.append(new_city)
print(cities)
# Ensure that the lat and lon valuse are all floats
print(type(new_city.lat), type(new_city.lon))

