import math
import Queue
import threading
import time
import sys
from init import hypergraph
import random
import string
import os

num_dim = input("Enter Number of Dimensions ")

no_of_nodes = int(math.pow(2, num_dim))
print"Number of nodes created = ",no_of_nodes
node_list=[]
Hypeobj=hypergraph(num_dim)
# print(node_list)
myNodes=Hypeobj.nodes
myEdges=Hypeobj.edges

print(myNodes)
print"Connected Edges are "

for x in myEdges:
    print(x)

no_of_threads = no_of_nodes
# raw_input("Press Enter to Continue Generating Threads")
def string_generator():
    sum=0
    y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    for x in y:
        # print(ord(x))
        sum = sum + ord(x)
    key=sum%no_of_nodes
    return key,y
hoplist=[]
exitFlag = 0
m=input("Enter (m) number of files to produce ")
p=input("Enter (p) number of files to retrieve that are associated with m and less then m ")
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
        files_produced = 0
        while files_produced < m:

            hop = -1
            # hoplist=[]
            data = threading.local()
            T1 = random.choice(range(10))
            time.sleep(T1)
            key, s = string_generator()
            k = bin(key)[2:].zfill(num_dim)
            for x in threading.enumerate():
                # sys.stdout.write(x.name+"\n")
                hop += 1
                if str(k) == str(x.name):
                    filename1 = str(threadName + 'KEY' + '.txt')
                    f1 = open(filename1, 'a+')
                    f1.write(str(key))
                    f1.close()
                    data.node = x.name
                    data.string = str(s) + " " + str(key)
                    filename2 = str(data.node) + '.txt'
                    f2 = open(filename2, 'a+')
                    f2.write("{" + threadName + " " + str(s) + " " + str(key) + "}" "\n")
                    f2.close()
                    hop=hop- 1

            hoplist.append(hop)
            files_produced = files_produced + 1
            sys.stdout.write("Generated by = " + threadName + " \'" + str(s) + "\'  Store in = " + str(k) + '\n')
            T2 = random.choice(range(10))
            time.sleep(T2)

        files_retrieved = 0

        while files_retrieved < p:
            #       #work a random time between 1 and 10 seconds // simulate user identifying file to
            T3 = random.choice(range(10))
            time.sleep(T3)
            filename1 = str(threadName + 'KEY' + '.txt')  # // keys previously produced
            f3 = open(filename1, 'r')
            N1 = random.choice(f3.read())
            filename2 = str(bin(int(N1))[2:].zfill(num_dim) + '.txt')
            x=random.choice(myNodes)
            nodes_killed = 0
            q=1
            r=1
            while nodes_killed<q:
                time.sleep(r)
                if x==threadName:
                    print(threadName+" Thread Killed by Main Thread (Evil Thread)\n")
                    threadName.__reduce__()
                    return
                else:
                    with open(filename2) as f:
                        content = f.readlines()
                        # print content
                        for x in content:
                            if threadName in x:
                                print ("Random string retrieved which is generated by "+x)
                    files_retrieved = files_retrieved+ 1
                    nodes_killed=nodes_killed+1

      else:
            queueLock.release()
            time.sleep(1)

threadList = myNodes
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
print "Average number of hops : ",(sum(hoplist) / len(hoplist))
print "Exiting All Threads"