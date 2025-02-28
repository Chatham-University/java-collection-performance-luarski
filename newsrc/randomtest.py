import random
import time
import array
from collections import deque

randomList = []
randomArray = array.array('i',[])
randomDeque = deque()
howManyInts = 100000
now = time.time()

for i in range(howManyInts):
	randomList.append(random.randint(1,howManyInts))
	randomList.append(random.randint(1,howManyInts))
	randomList.append(random.randint(1,howManyInts))
howLong = time.time() - now
print(f"That took {howLong}")

for i in range(howManyInts):
	randomArray.append(random.randint(1,howManyInts))
	randomArray.append(random.randint(1,howManyInts))
	randomArray.append(random.randint(1,howManyInts))
howLong = time.time() - now
print(f"That took {howLong}")

for i in range(howManyInts):
	randomDeque.append(random.randint(1,howManyInts))
	randomDeque.append(random.randint(1,howManyInts))
	randomDeque.append(random.randint(1,howManyInts))
howLong = time.time() - now
print(f"That took {howLong}")