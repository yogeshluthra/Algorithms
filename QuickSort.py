import numpy as np

def QuickSort(Array, N, i=0):
    """
    :param Array: the array to sort
    :param N: number of elements to work on for this step
    :param i: starting element for this step
    :return: none
    """
    if N<=1: return
    def swap(i,j):
        temp=Array[i]
        Array[i]=Array[j]
        Array[j]=temp

    # - choose pivot
    p = i

    # - start from a step ahead
    i+=1
    j=i

    # - partition around the pivot
    while j<p+N:
        if Array[j]<=Array[p]:
            swap(i,j)
            i+=1
        j+=1

    # - place the pivot at correct position
    swap(p,i-1) # i-1 is the highest index of elements <= Array[p]

    # - recurse on left
    QuickSort(Array, i-p-1, i=p)

    # - recurse on right
    QuickSort(Array, j-i, i=i)

for _ in range(20):
    N=10
    Array=list(np.random.randint(0,N, size=N))
    check_array=sorted(Array)
    print 'initial array    ', Array
    QuickSort(Array, N, i=0)
    print 'final array      ', Array
    print 'should be        ', check_array
    print
    assert check_array==Array
