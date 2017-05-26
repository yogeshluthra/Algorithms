import numpy as np
import matplotlib.pyplot as plt

class HashTable(object):

    def __init__(self, k, n=10000):
        """
        k: number of coefficients
        n: number of entries in the table
        """
        self.n=self.maxPrime_LessThan(n)    # size of table
        self.A=np.array([np.random.randint(low=1, high=self.n) for i in range(k)])
        self.table=[[] for i in range(self.n)]  # create the table of lists

    def Insert(self, key, val):
        """
        :param key: Must be a list of numbers (or numpy vector) of dimension k
        :param val: some value associated with the key (not used by the table in anyway. Depends on user for its use)
        """
        X=np.asarray(key, dtype=int)
        index=self.HashInput(X, self.A, self.n)
        for i, kv in enumerate(self.table[index]):
            k, v=kv
            if np.array_equal(X, k):
                print "W: {0} is seen before. value changed from {1} -> {2}".format(key, v, val)
                self.table[index][i][1]=val
                return
        self.table[index].append([X, val])

    def Lookup(self, key):
        X = np.asarray(key, dtype=int)
        index=self.HashInput(np.asarray(key, dtype=int), self.A, self.n)
        for k, v in self.table[index]:
            if np.array_equal(X, k):
                return v
        return None

    def Delete(self, key):
        X = np.asarray(key, dtype=int)
        index = self.HashInput(X, self.A, self.n)
        for i, k, v in enumerate(self.table[index]):
            if np.array_equal(X, k):
                del self.table[index][i]
                return

    def maxPrime_LessThan(self, N):
        """Returns max prime number <= N"""
        n=N
        while n>=2:
            if all(n%d for d in range(2, int(n**0.5 + 1))):
                return n
            n-=1

    def HashInput(self, X, A, n=9973):
        """
        HashInput function that accepts X, K dimensional vector, and returns an equivalent integer value, which is basically the hashed address in the table of 'n' linked lists.
        'A' refers to a specific hash function in the family of hash functions represented by HashInput.
        :param X: a K dimensional vector (numpy vector)
        :param A: Represents specific Hash function from family of Hash functions (numpy vector)
        :param n: length of the table
        :return: Hashed address
        """
        return np.mod(np.dot(X,A),n)

def encode(state, shape):
    """state vector is expanded from right to left (right=MSB)"""
    encodedState=0
    mult=1
    for dim in np.linspace(len(shape)-1,0,len(shape), dtype=int):
        encodedState += state[dim]*mult
        mult *= shape[dim]
    return encodedState

def decode(discreteState, shape):
    """decodes based on shape from right to left (right=MSB)"""
    decodedState=[]
    mult=1
    for dim in np.linspace(len(shape)-1,0,len(shape), dtype=int):
        remainder=discreteState % (mult*shape[dim])
        bit=remainder//mult
        decodedState.insert(0, bit)
        discreteState -= bit*mult
        mult *= shape[dim]

    return np.asarray(decodedState, dtype=int)

if __name__=="__main__":
    dimensions=4
    maxValPerDimension=50
    stateShape = np.ones(4, dtype=int)*50
    counts=1000000
    HT=HashTable(dimensions)
    for aCount in range(counts):
        encodedState=aCount
        currentKey=decode(encodedState, stateShape)
        HT.Insert(currentKey, aCount)

    collisions=[]
    for index in range(len(HT.table)):
        collisions.append(len(HT.table[index]))
    plt.scatter(range(len(HT.table)), collisions)
    plt.show()





