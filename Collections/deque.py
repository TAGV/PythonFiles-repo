from collections import deque

#This is a double ended queue, operations can be performed from both the sides

d = deque()
print(type(d))

d.append('a')
d.append(1)
d.append(2)
d.append([1,2])

d.appendleft((1,))
d.appendleft({'a':1,'b':2})

d.pop()
d.popleft()

d.reverse()
d.extend([1,2,3,4])
d.extendleft([4,5,6,7])

d.rotate(1)                 #Rotate by 1 place....
d.rotate(2)

d.clear()



print(d)