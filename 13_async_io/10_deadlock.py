import threading

lock = threading.Lock()
lock_b = threading.Lock()

def taskk1():
    with lock:
        print("task 1 acquired lock a")
        with lock_b:
            print("task1 acquired lock b")

def task2():
    with lock_b:
        print("task 2 acquired lock b")
        with lock:
            print("task2 acquired lock a")


t1 = threading.Thread(target=taskk1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()