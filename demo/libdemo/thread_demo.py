import threading
from threading import Thread


def printNumbers():
    for n in range(1, 10):
        print(n)


ct = threading.current_thread()
print(ct)

t1 = Thread(target=printNumbers)
t1.start()

t1.join()  # Wait for t1 to terminate

print("Count = ", threading.active_count())
