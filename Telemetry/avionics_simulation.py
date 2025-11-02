import numpy as np
import matplotlib.pyplot as plt


F = 50_000        # Thrust in Newtons (50 kN)
m = 1.3           # CubeSat mass (kg)
g = 9.81          # Gravity (m/s^2)
t_end = 16        # Telemetry stop time (sec)
dt = 1            # Time step (1 sec)
thrust_time = 10  # Thrust duration (sec)


t = np.arange(0, t_end + dt, dt)


v = np.zeros_like(t, dtype=float)
h = np.zeros_like(t, dtype=float)

# Simulation Loop
for i in range(1, len(t)):
    if t[i] <= thrust_time:
        a = (F / m) - g     # acceleration with thrust
    else:
        a = -g              # free fall after thrust cutoff

    v[i] = v[i-1] + a * dt
    h[i] = h[i-1] + v[i] * dt

#Find max altitude & velocity index
max_v_index = np.argmax(v)
max_h_index = np.argmax(h)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,7))

# Altitude Plot
ax1.plot(t, h, label="Altitude vs Time",color='blue')
ax1.scatter(t[max_h_index], h[max_h_index], marker='o', label="Max Altitude")
ax1.set_title("Altitude vs Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Altitude (m)")
ax1.grid(True)
ax1.legend()

# Velocity Plot
ax2.plot(t, v, label="Velocity vs Time", color='red')
ax2.scatter(t[max_v_index], v[max_v_index], marker='o', label="Max Velocity")
ax2.set_title("Velocity vs Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
