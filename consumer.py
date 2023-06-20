import random
import time

from threaded_base_class import ThreadedBaseClass
from threading import Thread
from multiprocessing import Queue


class Consumer(ThreadedBaseClass):
    def __init__(self):
        self.thread = None
        self.alive = None

    def start(self, data_queue: Queue):
        if self.alive:
            raise RuntimeWarning("Consumer thread is already running...")
        else:
            self.alive = True
            self.thread = Thread(target=self.target_method, args=[data_queue, ])
            self.thread.start()

    def stop(self):
        self.alive = False

    def target_method(self, data_queue: Queue):
        while self.alive:
            if data_queue.empty() is False:
                data = data_queue.get()
                print(f"Got new data: {data}")


