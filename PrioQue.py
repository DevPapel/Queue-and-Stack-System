from qsClass import PriorityQueue

# Priority Values #
Essential = 5
Critical = 4
Very_Important = 3
Important = 2
Neutral = 1
# End of Priority Values #

messages = PriorityQueue()
messages.enqueue_with_priority(Important, "after all these years")
messages.enqueue_with_priority(Very_Important, "I was wondering if")
messages.enqueue_with_priority(Neutral, "you'd like to meet")
messages.enqueue_with_priority(Essential, "Hello")
messages.enqueue_with_priority(Critical, "it's me")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())