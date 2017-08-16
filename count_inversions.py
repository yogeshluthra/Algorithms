
def mergesort_n_countInvIn(array):
    if len(array)==1: return (array, 0);
    halfLen=int(len(array)/2)
    arrayL, inversionsFromLeft=mergesort_n_countInvIn(array[:halfLen])
    arrayR, inversionsFromRight=mergesort_n_countInvIn(array[halfLen:])

    # merging routine
    lp=rp=0 # initialize left and right pointers
    inversionsHere=0
    newarray=[]
    while True:
        if arrayL[lp] > arrayR[rp]:
            #print "inversion: ({left}, {right})".format(left=arrayL[lp:], right=arrayR[rp])
            inversionsHere+=len(arrayL)-lp
            newarray.append(arrayR[rp])
            rp+=1
            if rp==len(arrayR):
                for anElement in arrayL[lp:]:
                    newarray.append(anElement)
                break;
        else:
            newarray.append(arrayL[lp])
            lp+=1
            if lp==len(arrayL):
                for anElement in arrayR[rp:]:
                    newarray.append(anElement)
                break;

    arrayL=arrayR=None # garbage collection
    return newarray, inversionsFromLeft+inversionsFromRight+inversionsHere

array=[]
#array=[1,3,5,2,4,6]
with open("data/assignment_week1.txt") as arrayFile:
    for line in arrayFile:
        array.append(int(line.strip()))
print len(array)
sortedArray, inversions=mergesort_n_countInvIn(array)
print len(sortedArray)
#print "sorted array: "+str(sortedArray)
print "number of inversions: "+str(inversions)
