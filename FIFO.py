from qsClass import Queue

FIFO = Queue("1", "2")
FIFO.enqueue("3")
FIFO.enqueue("4")
print("Queue Count:",len(FIFO))

for i in FIFO:
    print("Current in line:",i)

print("Updated Queue Count:", len(FIFO))