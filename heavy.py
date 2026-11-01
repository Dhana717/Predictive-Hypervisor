import time

data = bytearray(256 * 1024 * 1024)

print("Heavy workload started")

time.sleep(20)

for cycle in range(3):
    print("CPU burst:", cycle + 1)

    start = time.time()
    while time.time() - start < 15:
        for i in range(100000):
            x = i * i

    print("Idle period")
    time.sleep(15)

print("Heavy workload completed")
