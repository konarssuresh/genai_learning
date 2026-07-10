import threading
import requests
import time 


def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"finished downloading from {url} , size {len(resp.content)} bytes")

urls = [
    'https://picsum.photos/200/300',
    'https://picsum.photos/600/600',
    'https://picsum.photos/800/800'
]

start = time.time()

threads = [ threading.Thread(target=download,args=(url,)) for url in urls ]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

end = time.time()


print(f"Total time - {end-start:.2f}")

for url in urls:
    download(url)

new_end = time.time()

print(f"sync time taken {new_end-end:.2f}")