import queue
import threading
import time

q = queue.Queue(maxsize=10)

def producer():
    for i in range(10):
        q.put(i)
        print("Produced:", i)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        print ("Consumed:", item)
        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All tasks are done.")