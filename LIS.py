
'''Longest increasing sequence'''

class LIS(object):

    def __init__(self, seq=[5,2,8,6,3,6,9,7]):
        self.seq=seq
        self.parent=[i for i in range(len(seq))] # the list of parent addresses.. That is, element i contains index of its parent that forms the longest sequence upto i
        self.L=[0]*len(seq) # initialize longest sub-sequences to 0

        self.max_subLength, self.max_subLength_index=0, 0
        for i in range(len(seq)):
            self.L[i] += 1 # add for 1 for self
            # - find maximum length sub-sequence from previous solved problems
            curr_max_subLength=0
            for j in range(i):
                if seq[j] < seq[i]: # there is an edge
                    if curr_max_subLength < self.L[j]: # found new max sub length
                        curr_max_subLength = self.L[j]
                        self.parent[i]=j
            self.L[i] += curr_max_subLength
            # - book keeping to track of longest sub-sequence
            if self.max_subLength < self.L[i]:
                self.max_subLength = self.L[i]
                self.max_subLength_index = i

    def printLIS(self):
        print self.seq
        print [i for i in range(len(self.seq))]
        print
        print 'parents\n', self.parent
        print 'max sub lengths\n', self.L
        print
        print 'max sub length sequence is:'
        i=self.max_subLength_index
        maxSubSeq=[]
        while i!=self.parent[i]:
            maxSubSeq.append(self.seq[i])
            i=self.parent[i]
        maxSubSeq.append(self.seq[i])
        print maxSubSeq[::-1]

lis=LIS()
lis.printLIS()