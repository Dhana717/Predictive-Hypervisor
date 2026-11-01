
import psutil
import csv
import time
from datetime import datetime

vm_name = input("Enter VM name (Heavy/Light): ")
filename = vm_name.lower() + "_simultaneous_metrics.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Timestamp", "CPU_Usage", "RAM_Usage", "RAM_Used_MB"])

    for i in range(60):
        cpu = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()
        ram_percent = memory.percent
        ram_used = memory.used / (1024 * 1024)

        timestamp = datetime.now().strftime("%H:%M:%S")

        writer.writerow([timestamp, cpu, ram_percent, round(ram_used, 2)])

        print("CPU:", cpu, "% | RAM:", ram_percent, "%")

        time.sleep(1)

print("Monitoring completed!")
print("Data saved in:", filename)
