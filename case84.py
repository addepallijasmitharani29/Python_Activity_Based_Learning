
# Case 84: Environmental Monitoring Data Analyzer

records = []

for day in range(5):
    print("\nDay", day + 1)

    temperature = float(input("Enter temperature in Celsius: "))
    aqi = int(input("Enter AQI: "))
    water_quality = float(input("Enter water quality value: "))

    records.append((temperature, aqi, water_quality))

print("\n--- Environmental Report ---")

for i in range(len(records)):
    temperature, aqi, water_quality = records[i]

    print("\nDay", i + 1)
    print("Temperature:", temperature)
    print("AQI:", aqi)
    print("Water Quality:", water_quality)

    if temperature > 40 or aqi > 100 or water_quality < 50:
        print("Status: Environmental Alert")
    else:
        print("Status: Normal")

average_temperature = sum(record[0] for record in records) / len(records)
average_aqi = sum(record[1] for record in records) / len(records)

print("\nAverage Temperature:", average_temperature)
print("Average AQI:", average_aqi)
