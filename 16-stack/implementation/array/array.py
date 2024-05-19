def push(data):
    global stack 
    global top
    global stackMax
    top = top + 1
    if top > 10000:
        print("Stack Is Full")
    else:
        stack.append(data)  
def pop():
    global stack 
    global top
    global stackMax
    if top <= -1:
        print("Stack Is Empty")
    else:
        stack.pop()  
        top = top - 1

def display():
    global stack 
    global top
    global stackMax
    if top <= -1:
        print("-1")
    else:
        i = 0
        while i <= top:
            print(stack[i], end=" ")
            i = i + 1
        print()

stack = []
top = -1
stackMax = 10000

push(10)
push(20)
push(10)
push(10)
display()
