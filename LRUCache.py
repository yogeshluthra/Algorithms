import numpy as np

'''Least Recently Used (https://leetcode.com/problems/lru-cache/description/)'''

class Node(object):
    """a Node in doubly linked list"""
    def __init__(self, key):
        self.key=key
        self.head=None
        self.tail=None

class LRUCache(object):
    def __init__(self, capacity, verbose=False):
        """
        :type capacity: int
        """
        assert capacity>0
        self.dataDict = {}  # stores key: [value, location in eleAccessIndex]
        self.Nele = 0  # current number of elements in LRUCache
        self.capacity = capacity
        # Doubly linked List. just helps to locate least accessed element
        self.histHead=None
        self.histTail = None
        self.verbose=verbose

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dataDict and self.Nele > 0:
            value, node = self.dataDict[key]
            # take the node out from the list
            self.TakeOutNode(node)
            self.InsertNode(key, value)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dataDict:
            if self.Nele < self.capacity:  # if not at capacity
                self.InsertNode(key, value)
            else:  # if at capacity
                # take out the least element from dictionary
                tailKey=self.histTail.key
                removedVal,node=self.dataDict.pop(tailKey)
                if self.verbose:    print '\npopped ',tailKey,removedVal,'\n'
                self.TakeOutNode(node)
                self.InsertNode(key, value)
        else:
            node=self.dataDict[key][1]
            # take the node out from the list
            self.TakeOutNode(node)
            self.InsertNode(key, value)

    def InsertNode(self, key, value):
        """Insert node in at top of running history of nodes"""
        newNode = Node(key)
        if self.Nele!=0:
            self.histHead.head=newNode
            newNode.tail=self.histHead
        else:
            self.histTail=newNode
        self.histHead=newNode
        self.dataDict[key] = [value, newNode]
        self.Nele +=1

    def TakeOutNode(self, node):
        """take out node from anywhere in last history, while maintaining the list"""
        assert node is not None

        if node.tail is not None: # some intermediate node
            node.tail.head = node.head
        else: # need to take care of histTail
            self.histTail=node.head

        if node.head is not None: # some intermediate node
            node.head.tail = node.tail
        else: # need to take care of histHead
            self.histHead=node.tail

        self.Nele -=1
        node = None  # delete the node

    def printKeyHist(self):
        node=self.histTail
        print 'History'
        while node is not None:
            print node.key,
            node=node.head
        print '\n'


if __name__=="__main__":
    ops=["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put",
                 "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
                 "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put",
                 "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put",
                 "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put",
                 "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put",
                 "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put",
                 "put", "put", "put", "put", "put", "put"]
    data=[[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
                 [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3],
                 [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27],
                 [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10],
                 [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4],
                 [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5],
                 [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5],
                 [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
    expected=[None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
    # ops=["LRUCache", "put", "get", "put", "get", "get"]
    # data=[[1], [2, 1], [2], [3, 2], [2], [3]]
    # expected=[None, None, 1, None, -1, 2]


    obj=None
    output=[]
    for i, op in enumerate(ops):
        value = None
        if op == 'LRUCache':
            capacity=data[i][0]
            obj = LRUCache(capacity, verbose=False)
        elif op=='put':
            obj.put(data[i][0], data[i][1])
        elif op=='get':
            value=obj.get(data[i][0])
        output.append(value)
        print ops[i], '(', data[i], ')  --> ', expected[i], ' ', output[i]
        obj.printKeyHist()


    # Your LRUCache object will be instantiated and called as such:
    #
    # param_1 = obj.get(key)
    # obj.put(key,value)