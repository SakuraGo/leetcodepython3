from queue import Queue #LILO队列
import numpy as np



stackss = [1,2,3,5]
stackss.pop()
stackss.__repr__()
stackss.remove(3)

q=Queue()


q.put(35)
q.put(3)
print(q)
