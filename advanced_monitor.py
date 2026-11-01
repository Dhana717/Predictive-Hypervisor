import psutil
import csv
import time
from datetime import datetime

def read_vmstat():
    values = {}
    with open("/proc/vmstat") as file:
        for line in file:
            key, value = line.split()
            if key in ["pgfault", "pgmajfault"]:
                values[key] = int(value)
    return values

def read_cpu_stats():
    values = {}
    with open("/proc/stat") as file:
        for line in file:
            parts = line.split()
            if parts[0] in ["ctxt", "intr", "procs_running"]:
                values[parts[0]] = int(parts[1])
    return values

def read_memory_pressure():
    try:
        with open("/proc/pressure/memory") as file:
            for line in file:
                if line.startswith("some "):
                    parts = line.split()
                    return float(parts[1].split("=")[1])
    except FileNotFoundError:
        return 0.0
    return 0.0

vm_name = input("Enter VM name (Heavy/Light): ")
filename = vm_name.lower() + "_advanced_metrics.csv"

previous_vm = read_vmstat()
previous_cpu = read_cpu_stats()
previous_disk = psutil.disk_io_counters()

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Timestamp", "CPU_Usage", "RAM_Usage",
        "PageFault_Rate", "MajorFault_Rate",
        "ContextSwitch_Rate", "Interrupt_Rate",
        "Running_Processes", "Memory_Pressure",
        "Disk_Read_Rate_MB", "Disk_Write_Rate_MB"
    ])

    for i in range(60):
        start = time.time()

        cpu = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()

        current_vm = read_vmstat()
        current_cpu = read_cpu_stats()
        current_disk = psutil.disk_io_counters()

        page_fault_rate = current_vm["pgfault"] - previous_vm["pgfault"]
        major_fault_rate = current_vm["pgmajfault"] - previous_vm["pgmajfault"]

        context_rate = current_cpu["ctxt"] - previous_cpu["ctxt"]
        interrupt_rate = current_cpu["intr"] - previous_cpu["intr"]

        read_rate = (current_disk.read_bytes - previous_disk.read_bytes) / (1024 * 1024)
        write_rate = (current_disk.write_bytes - previous_disk.write_bytes) / (1024 * 1024)

        pressure = read_memory_pressure()

        timestamp = datetime.now().strftime("%H:%M:%S")

        writer.writerow([
            timestamp,
            cpu,
            memory.percent,
            page_fault_rate,
            major_fault_rate,
            context_rate,
            interrupt_rate,
            current_cpu["procs_running"],
            pressure,
            round(read_rate, 3),
            round(write_rate, 3)
        ])

        print("CPU:", cpu, "% | RAM:", memory.percent,
              "% | Page faults:", page_fault_rate,
              "| Memory pressure:", pressure)

        previous_vm = current_vm
        previous_cpu = current_cpu
        previous_disk = current_disk

        elapsed = time.time() - start
        time.sleep(max(0, 2 - elapsed))

print("Advanced monitoring completed!")
print("Data saved in:", filename)
