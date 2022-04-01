import csv
import random

num_iterations = 560000

with open('fake_weather.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['latitude', 'longitude', 'fuel_type', 'capacity_factor'])
    for i in range(num_iterations):
        lat = random.randint(23, 49) + (random.randint(0, 100) / 100)
        lon = random.randint(-126, -61) + (random.randint(0, 100) / 100)
        if random.randint(0, 1):
            fuel_type = 'Solar'
        else:
            fuel_type = 'Wind'
        capacity_factor = random.randint(2, 60) / 100
        output = [lat, lon, fuel_type, capacity_factor]
        writer.writerow(output)
