# Case-Study-2
Temperature-Monitoring

Problem Statement

Design a Python-based Temperature Monitoring System that simulates an IoT temperature sensor.

The system should:

Accept minimum and maximum temperature limits from the user.

Generate random temperature readings at every 2-second interval.

Compare each temperature reading with the defined limits.

Display appropriate alert messages if the temperature goes below or above the specified range.


Approach

Import required modules:

random → To generate random temperature values.

time → To create a 2-second delay between readings.

Accept input from user:

Minimum temperature limit.

Maximum temperature limit.

Generate random temperature values (e.g., between 0°C and 100°C).

Use conditional statements:

If temperature < minimum limit → Display Low Temperature Alert

If temperature > maximum limit → Display High Temperature Alert
CODE

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
OUTPUT

Enter minimum temperature limit: 37
Enter maximum temperature limit: 50

Temperature monitoring started...

Current Temperature: 70°C
Alert: Temperature is too high!

Current Temperature: 29°C
Alert: Temperature is too low!

Current Temperature: 63°C
Alert: Temperature is too high!

Current Temperature: 63°C
Alert: Temperature is too high!

Current Temperature: 8°C
Alert: Temperature is too low!

Otherwise → Display Temperature within Safe Range

Repeat the process every 2 seconds to simulate real-time monitoring.
