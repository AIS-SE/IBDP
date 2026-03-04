#queue implementation using an array pg357
queue = [0] * 6
frontPointer = 0
endPointer = -1
queueSize = 6
queueLength = 0
def queueEmpty():
    if(queueLength==0):
        return True
    else:
        return False
def queueFull():
    if(queueLength<queueSize):
        return False
    else:
        return True
# Add an element to the queue
def enqueue(val):
    global endPointer,queueLength
    if queueFull():
        print("You can't enqueue")
    else:
        endPointer = endPointer + 1
        queue[endPointer] = val
        queueLength = queueLength + 1
        print("You added:", val)
def dequeue():
    global frontPointer, queueLength, endPointer
    if(queueEmpty()):
            print("You can't dequeue")
    else:
        val = queue[frontPointer]
        print("You removed", queue[frontPointer])
        frontPointer = frontPointer+1
        queueLength = queueLength-1
        endPointer = endPointer-1
        return val
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)
print("Values in queue: ", queue)
