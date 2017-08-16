import numpy as np
import time
'''Find Min Cut in given graph.'''
class edge(object):
    def __init__(self, A, B):
        self.A=A
        self.B=B
    def getA(self):
        return self.A
    def getB(self):
        return self.B

def deleteEdge(delJ, fromArray, usingI):
    """
    delete edge j fromArray with starting index i.
    """
    temp = fromArray[delJ]
    fromArray[delJ] = fromArray[usingI]
    fromArray[usingI] = temp
    usingI+=1
    return usingI

def contractEdge(ArrayOfEdges, ind):
    """
    contractEdge ( in ArrayOfEdges, for the edge at index ind) where node indices are associated by indexTree. \n
    This function implements weighted union routine.
    """
    nodeA=ArrayOfEdges[ind].getA()
    rootA=root(nodeA)

    nodeB=ArrayOfEdges[ind].getB()
    rootB=root(nodeB)

    if rootA == rootB:
        raise ValueError('{0} and {1} already belong to same root {3}\n\t they should not be contracted'.format(nodeA, nodeB, rootA))

    if szTree[rootA] < szTree[rootB]: indexTree[rootA]=rootB; szTree[rootB]+=szTree[rootA];
    else                            : indexTree[rootB]=rootA; szTree[rootA]+=szTree[rootB];


def root(index):
    """
    find root for index in indexTree \n
    This method implements path compression to reduce cost for subsequent root searches.
    """
    while indexTree[index]!=index:
        indexTree[index]=indexTree[indexTree[index]]   # path compression
        index=indexTree[index]
    return index

N=200
Org_ArrayOfEdges=[]
M=0
nodeTrackerArray=[False]*(N+1)
nodeCounter=0
with open('data/week3_data.txt') as dataFile:
    for aRow in dataFile:
        currRowContents=aRow.split()
        nodeA=int(currRowContents[0].strip())               # Current node is nodeA
        for i in range(1, len(currRowContents)):    # scan adjacent nodes to nodeA.
            nodeB=int(currRowContents[i].strip())
            if nodeTrackerArray[nodeB] is False:    # Check if nodeB was already seen. If not, Create an edge and add to list
                newEdge=edge(nodeA, nodeB)
                Org_ArrayOfEdges.append(newEdge)
                M+=1
                print 'ADDING edge {0} <-> {1}'.format(nodeA, nodeB)
            else:
                print 'SKIPPING edge {0} <-> {1}'.format(nodeA, nodeB)
        nodeTrackerArray[nodeA]=True
        nodeCounter+=1

if nodeCounter != N:
    raise ValueError('counted # nodes are not equal to expected # nodes.')

print 'found {0} nodes and {1} edges'.format(N,M)

randomRuns=N*N
minCutEdges=float("inf")
indexTree=[]
szTree=[]

starttime=time.time()
for aRun in range(randomRuns):
    print 'run {0} in {1}'.format(aRun, time.time()-starttime)
    # Create an index map to keep track of contractions.
    # When node B is contracted into node A --> RealIndexOf(B) = RealIndexOf(A)
    #   and all remaining edges in ArrayOfEdges is scanned to self loop deletions.
    indexTree=[i for i in range(N+1)]
    szTree=[1 for i in range(N+1)]

    currN=N
    lowestEdgeInd=0
    while currN > 2:
        j=np.random.randint(lowestEdgeInd, M)
        contractEdge(Org_ArrayOfEdges, j)       # contraction simply makes nodes as connected components.
        currN=currN-1
        k=lowestEdgeInd
        while k < M:        # scan array of m edges for self loops
            nodeA=Org_ArrayOfEdges[k].getA();
            nodeB=Org_ArrayOfEdges[k].getB();
            if root(nodeA) == root(nodeB):      # check if nodes of current edge are connected components
                lowestEdgeInd=deleteEdge(k, Org_ArrayOfEdges, lowestEdgeInd)    # if they are, delete that edge (this is a self loop)
            k+=1
    if minCutEdges > M-lowestEdgeInd:
        minCutEdges=M-lowestEdgeInd
        print 'New remaining edges {0}'.format(minCutEdges)
        # sanity checks
        remainingNodes=set()
        for i in range(M):
            nodeA=Org_ArrayOfEdges[i].getA()
            nodeB=Org_ArrayOfEdges[i].getB()
            remainingNodes.add(root(nodeA))
            remainingNodes.add(root(nodeB))
        print remainingNodes
