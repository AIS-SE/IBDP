#Stack implementation using an array
stackSize = 7
stack = [""] * stackSize
topIndex = -1
def isEmpty():
    if topIndex == -1:
        return True
    else:
        return False
def isFull():
    if topIndex == stackSize - 1:
        return True
    else:
        return False
def push(value):
    global topIndex
    if isFull():
        print("Stack Overflow")
    else:
        topIndex += 1
        stack[topIndex] = value
def pop():
    global topIndex
    if isEmpty():
        print("Stack Underflow")
    else:
        topIndex -= 1
def peek():
    print(stack[topIndex])
push("word1")
push("word2")
push("word3")
push("word4")
push("word5")
peek()
pop()
pop()
peek()
