import random
import time
import matplotlib.pyplot as plt

# Lists to store data
time_data = []
temp_data = []
volt_data = []
curr_data = []

plt.ion()  # Turn interactive mode ON
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 8))

t = 0

while True:  # infinite real-time loop
    t += 1

    # Generate random telemetry values
    temp = random.uniform(10, 50)    # Temperature (°C)
    volt = random.uniform(3.3, 8.4)  # Voltage (Volts)
    curr = random.uniform(0.0, 2.0)  # Current (Amps)

    # Append new values
    time_data.append(t)
    temp_data.append(temp)
    volt_data.append(volt)
    curr_data.append(curr)

    # Clear previous plots
    ax1.cla()
    ax2.cla()
    ax3.cla()

    # Plot temperature
    ax1.plot(time_data, temp_data)
    ax1.set_title("Live CubeSat Telemetry")
    ax1.set_ylabel("Temp (°C)")

    # Plot voltage
    ax2.plot(time_data, volt_data)
    ax2.set_ylabel("Voltage (V)")

    # Plot current
    ax3.plot(time_data, curr_data)
    ax3.set_ylabel("Current (A)")
    ax3.set_xlabel("Time (s)")

    plt.tight_layout()
    plt.pause(1)  # updates every 1 second

