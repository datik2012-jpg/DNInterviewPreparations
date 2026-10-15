from collections import deque






if __name__ == "__main__":
    print("Queue example:")
    
    d = deque()
    
    d.append(10)
    d.append(20)
    d.append(30)
    d.append(40)
    
    
    first = d.popleft()
    print(f"Return left: {first}") #get first whe we insrert  - # 10
    
    last = d.pop() #get the last we insert # 40
    print(f"Return right:{last}")
    
    