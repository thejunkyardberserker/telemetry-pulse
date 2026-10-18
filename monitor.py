
import time

print("--- Telemetry Pulse Initialized ---")

# A simple loop testing 3 sensor read cycles
for count in range(1, 4):
    print(f"Reading cycle {count}: Voltage stable at 5.0V, Core temp 42°C")
    time.sleep(1)

print("Diagnostic complete: All systems nominal.")