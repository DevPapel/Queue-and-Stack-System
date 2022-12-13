from qsClass import PriorityQueue

# Priority Values #
Essential = 5
Critical = 4
Very_Important = 3
Important = 2
Neutral = 1
# End of Priority Values #

messages = PriorityQueue()
messages.enqueue_with_priority(Important, "Windshield wipers turned on")
messages.enqueue_with_priority(Very_Important, "Radio station tuned in")
messages.enqueue_with_priority(Essential, "Brake pedal depressed")
messages.enqueue_with_priority(Critical, "Hazard lights turned on")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())