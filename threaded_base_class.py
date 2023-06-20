from abc import ABC, abstractmethod
from threading import Thread


class ThreadedBaseClass(ABC):
    def __int__(self):
        self.alive: bool
        self.thread: Thread

    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def target_method(self):
        raise NotImplementedError
