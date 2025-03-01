#!/usr/bin/env python3
import time
import threading

def cpu_intensive_task():
    while True:
        sum(i * i for i in range(10000))

# Start multiple threads to simulate load
threads = []
for _ in range(2):  # Adjust the number of threads as needed
    thread = threading.Thread(target=cpu_intensive_task)
    thread.start()
    threads.append(thread)

# Run for a specified duration
time.sleep(60)
