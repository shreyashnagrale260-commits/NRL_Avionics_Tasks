import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.arange(0, 200, 1)  # 200 seconds simulation

# Simulated satellite elevation angles (degrees)
# Station A sees satellite first, then loses it
elev_A = 50 * np.sin(0.03 * t)  

# Station B sees satellite later
elev_B = 50 * np.sin(0.03 * t - 1.5)

handover_time = None

for i in range(len(t)):
    if elev_A[i] < 0 and elev_B[i] > 0:
        handover_time = t[i]
        break

print("Handover occurs at t =", handover_time, "seconds")

# Plot
plt.figure(figsize=(8,5))
plt.plot(t, elev_A, label="Ground Station A",color='green')
plt.plot(t, elev_B, label="Ground Station B",color='red')

plt.axvline(handover_time, linestyle="--", label="Handover Point")
plt.xlabel("Time (s)")
plt.ylabel("Elevation Angle (°)")
plt.title("Ground Station Handover Simulation")
plt.legend()
plt.grid(True)
plt.show()
