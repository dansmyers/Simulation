"""

Heap class 

Helped by Noah 

"""
class Heap:

    heap = []

    def __init__(self,array):
        self.heap = array
        self.buildHeap()

    def siftUp(self,i):
        pni = ((i - 1) // 2)                                    #  get parent node index
        if(pni >= 0):                                           #  if parent index >= 0, index is not root - compare
            if(self.heap[i][0] < self.heap[pni][0]):            #  if index time value is less than parent time value
                self.heap[i], self.heap[pni] = self.heap[pni], self.heap[i]         #  swap index and parent tuple values
                self.siftUp(pni)                                #  call sift up again on parent index

    def swapCildren(self,i):
        lci = ((2 * i) + 1)                                     #  get left child index
        rci = ((2 * i) + 2)                                     #  get right child index
        if((self.heap[i][0] > self.heap[lci][0]) or (self.heap[i][0] > self.heap[rci][0])):         #  if index > left or right
            if(self.heap[lci][0] <= self.heap[rci][0]):         #  if left time value is less than or equal to right time value
                self.heap[i], self.heap[lci] = self.heap[lci], self.heap[i]         #  swap index and left tuple values
                self.siftDown(lci)                              #  call sift down again on left child index
            else:                                               #  else right time is less than left time
                self.heap[i], self.heap[rci] = self.heap[rci], self.heap[i]         #  swap index and right tuple values
                self.siftDown(rci)                              #  call sift down again on right child index

    def siftDown(self,i):
        lli = ((len(self.heap) // 2) - 1)                       #  get last non-leaf node index
        if(lli > i):                                            #  if index is less than the last non-leaf index
            self.swapCildren(i)
        if(lli == i):                                           #  if the index is the last non-leaf index
            if((len(self.heap) & 1) == 1):                      #  if heap size is odd last non-leaf has two children
                self.swapCildren(i)
            else:                                               #  else last non-leaf has one child (left)
                lci = ((2 * i) + 1)                             #  get left child index
                if(self.heap[i][0] > self.heap[lci][0]):        #  if index time value greater than left time value
                    self.heap[i], self.heap[lci] = self.heap[lci], self.heap[i]     #  swap index and left tuple values

    def buildHeap(self):
        for i in range((((len(self.heap)) // 2) - 1), -1, -1):  #  iterate backwards through the non-leaf nodes indexes
            self.siftDown(i)

    def insert(self,node):
        self.heap.append(node)                                  #  append the new node to the bottom of the heap
        self.siftUp((len(self.heap) - 1))                       #  sift the last index (newly placed node) up the list

    def pop(self):
        value = self.heap[0]                                    #  set root as value to return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]                   #  swap root and last values
        self.heap = self.heap[:-1]                              #  remove last value from heap (swaped root)
        self.siftDown(0)                                        #  sift down the swaped last value
        return(value)                                           #  return the original root

####  MAIN  ####################################################################################################################

def main():
    testHeap = Heap([(17.3,"stuff"),(15.15,"other stuff"),(8.8,"more stuff"),(9.13,"less stuff"),(10.0,"red stuff"),
                    (13.13,"blue stuff"),(6.67,"left stuff"),(4.4,"right stuff"),(5.4,"up stuff"),(3.2,"down stuff")])
    print(testHeap.heap)
    testHeap.insert((1.1,"around stuff"))
    print(testHeap.heap)
    event = testHeap.pop()
    print(event)
    event = testHeap.pop()
    print(event)
    event = testHeap.pop()
    print(event)
    testHeap.insert((7.77,"lucky stuff"))
    testHeap.insert((5.4,"stuffing"))
    testHeap.insert((19.56,"dressing"))
    print(testHeap.heap)
    for i in range(len(testHeap.heap)):
        print(testHeap.pop())

if(__name__=="__main__"): main()