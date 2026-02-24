import random
import time
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\nTemperature monitoring started...\n")

while True:
    temperature = random.randint(0, 100)
    print(f"Current Temperature: {temperature}°C")
    if temperature > max_temp:
        print("Alert: Temperature is too high!\n")
    elif temperature < min_temp:
        print("Alert: Temperature is too low!\n")
    else:
        print("Temperature is normal.\n")
    time.sleep(2)