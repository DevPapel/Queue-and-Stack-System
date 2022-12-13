from queueclass import Queue

bounceSize = 3

que = input("Enter your name to line up the queue: ")

queList = [1,2,3]
if len(queList) < bounceSize:
    queList.append(que)
else:
    FIFO = Queue(queList)
    print(len(queList))
    print(len(FIFO))
