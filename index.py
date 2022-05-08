import threading
import time

class LazyMoverThread(threading.Thread):
    def __init__(self, threadId, name, count):
            threading.Thread.__init__(self)
            self.threadId = threadId
            self.name = name
            self.count = count
    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        toLoading(self.name, self.count)
        threadLock.release()
        print("Finished the work: " + self.name + "\n")

class TruckThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("the truk has arrived: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        toWaiting(self.name, self.count)
        print("the car is gone: " + self.name + "\n")


class MoverThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        toUploading(self.name, self.count)
        print("Finished the work: " + self.name + "\n")


def toLoading(name, count):
    while count:
        time.sleep(1)
        print('Loading...')
        count -= 1


def toUploading(name, count):
    while count:
        time.sleep(1)
        print('Uploading...')
        count -= 1


def toWaiting(name, count):
    while count:
        time.sleep(1)
        print('Truck\'s waiting...')
        count -= 1

threadLock = threading.Lock()

mover1 = LazyMoverThread(1, "loadingMover1", 5)
mover2 = LazyMoverThread(2, "loadingMover2", 5)
mover3 = LazyMoverThread(3, "loadingMover3", 5)

truck = TruckThread(7, "truck7",16)
truck2 = TruckThread(8, "truck8", 16)

mover4 = MoverThread(4, "uploadingMover4", 5)
mover5 = MoverThread(5, "uploadingMover5", 5)
mover6 = MoverThread(6, "uploadingMover6", 5)


truck.start()
loading_start = time.time()
mover1.start()
mover2.start()
mover3.start()

mover1.join()
mover2.join()
mover3.join()
loading_end = time.time() - loading_start
truck.join()



truck2.start()
uploading_start = time.time()
mover4.start()
mover5.start()
mover6.start()

mover4.join()
mover5.join()
mover6.join()
uploading_end = time.time() - uploading_start
truck2.join()

print('total loading time: ' , round(loading_end, 5))
print('total uploading time: ' , round(uploading_end, 5))