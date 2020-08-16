from math import radians, cos, sin, asin, sqrt


def distance(lat1, lat2, long1, long2):
    long1 = radians(long1)
    long2 = radians(long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    diff_long = long2 - long1
    diff_lat = lat2 - lat1
    x = sin(diff_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(diff_long / 2) ** 2
    y = 2 * asin(sqrt(x))
    radius = 6371
    return y * radius


latitude1 = float(input("Enter the latitude of first place: "))
longitude1 = float(input("Enter the longitude of first place: "))
latitude2 = float(input("Enter the latitude of second place: "))
longitude2 = float(input("Enter the longitude of second place: "))
print("The distance between place 1 and place 2 is ", distance(latitude1, latitude2, longitude1, longitude2),
      "kilometers.")
