import threading
from multiprocessing import Process
import time 

def cpu_heavy():
    print(f"Crunching some numbers")
    total = 0
    for i in range(10**8):
        total+=i
    print("Done")


start = time.time()

threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# [thread.start() for thread in threads]
# [thread.join() for thread in threads]
# print(f"thread time taken {time.time()-start:.2f}")

if __name__ == '__main__':
    processes = [Process(target=cpu_heavy) for _ in range(2) ]
    [process.start() for process in processes]
    [process.join() for process in processes]
    print(f"process time taken = {time.time()-start:.2f}")