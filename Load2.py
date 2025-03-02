import multiprocessing

def cpu_stress():
    while True:
        pass  # Infinite loop to consume CPU

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get the number of CPU cores
    processes = []
    
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()  # Keep processes running
