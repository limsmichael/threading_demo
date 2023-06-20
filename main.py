import time
from multiprocessing import Queue
from producer import Producer
from consumer import Consumer

def main():
    data_queue = Queue(maxsize=10)

    producer = Producer()
    producer.start(data_queue)

    consumer = Consumer()
    consumer.start(data_queue)

    time.sleep(5)
    print("Shutting down...")
    producer.stop()
    consumer.stop()
    data_queue.close()
    print("Shutdown")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()