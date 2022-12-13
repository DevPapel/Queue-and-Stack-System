from queueclass import Queue

FIFO = Queue("1", "2")
FIFO.enqueue("3")
print(len(FIFO))

