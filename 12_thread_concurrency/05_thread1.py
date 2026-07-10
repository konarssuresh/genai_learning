import threading
import time

def boil_milk():
    print("start boiling")
    time.sleep(2)
    print("milk boiled")

def toast_bun():
    print("start toasting bun")
    time.sleep(3)
    print("bun toasting done")

start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target = toast_bun)
t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"time taken - {end-start:.2f} seconds")