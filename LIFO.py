from qsClass import Stack

LIFO = Stack("test1","test2")
LIFO.enqueue("test3")
print("Current number in line:",len(LIFO))

for i in LIFO:
    print("Current in line:",i)

print("Current number in line:",len(LIFO))
