from collections import deque

qu = deque()
qu.append(1)
qu.append(2)
print(qu.popleft())
print(qu)