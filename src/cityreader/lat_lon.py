import csv

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  
  def __str__(self):
    return f'{self.name}, Lat: {self.lat}, Lon: {self.lon}'

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  out = open('cities.csv', 'r')
  data = csv.reader(out)
  data = [row for row in data]
  out.close()
  # Ensure that the lat and lon valuse are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  for x in range(1,len(data)):
    new_city = City(data[x][0], float(data[x][3]), float(data[x][4]))
    cities.append(new_city)
        
  return cities


# read the file
out = open('cities.csv', 'r')
data = csv.reader(out)
data = [row for row in data]
out.close()

# transfer data into a city objects and store in a list
cities = []
for x in range(1,len(data)):
    new_city = City(data[x][0], float(data[x][3]), float(data[x][4])) # last two are lat and lon

    cities.append(new_city)


lat1 = 40
lon1 = 100
lat2 = 60
lon2 = 120

lat_inrange = False
lon_inrange = False

my_city = cities[0]

city_lat = my_city.lat
city_lon = my_city.lon


if lat1 < lat2:
    if city_lat > lat1 and city_lat < lat2:
        lat_inrange = True
if lat1 > lat2:
    if city_lat < lat1 and city_lat > lat2:
        lat_inrange = True 
if lon1 < lon2:
    if city_lon > lon1 and city_lon < lon2:
        lon_inrange = True
if lon1 > lon2:
    if city_lon < lon1 and city_lon > lon2:
        lon_inrange = True

in_square = False

if lat_inrange == True and lon_inrange == True:
    in_square = True

print(in_square)