from multiprocessing import Process
import time 

def crunch_number():
    print(f"Started the count process.....")
    count = 0
    for _ in range(100_000_000):
        count +=1

    print("ended the count process...")
if __name__ == '__main__':
    start = time.time()

    p1=Process(target=crunch_number,name = "Process1")
    p2=Process(target=crunch_number,name = "Process1")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f" titak tine with multiprocessing is {end-start:.2f} seconds")