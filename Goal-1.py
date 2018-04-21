import math
import Queue
import threading
import time
import sys
from init import hypergraph


num_dim = input("Enter Number of Dimensions ")

no_of_nodes = int(math.pow(2, num_dim))
print"Number of nodes created = ",no_of_nodes



node_list=[]
for i in range(no_of_nodes):
    node_list.append(bin(i)[2:].zfill(num_dim))

if num_dim<6:
    Hypeobj = hypergraph(num_dim)
    myNodes = Hypeobj.nodes
    print(myNodes)
    myEdges = Hypeobj.edges
    print"Connected Edges are "
    for x in myEdges:
        print(x)
else: myNodes=node_list

no_of_threads = no_of_nodes
raw_input("Press Enter to Continue Generating Threads")

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print "Starting " + self.name
      process_data(self.name, self.q)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        queueLock.release()
        #
      else:
        queueLock.release()
      time.sleep(1)

threadList = []
for i in range(0,no_of_threads):
    threadList.append("Thread "+str(i)+" as "+str(bin(i)[2:].zfill(num_dim)))
nameList = myNodes
queueLock = threading.Lock()
workQueue = Queue.Queue()
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print "Exiting All Threads"