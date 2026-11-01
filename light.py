import time

data = bytearray(32 * 1024 * 1024)

print("Light workload started")

start = time.time()

while time.time() - start < 130:
    for i in range(2000):
        x = i * i

    time.sleep(0.2)

print("Light workload completed")
