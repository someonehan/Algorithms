import sys

def Merge(A, p, q, r):
    """merge two part of the list into list
    
    args:
        A : the list to be ordered
        p : the start index of A
        q : the center index of A
        r : the end index of A
    """

    lenl = q - p + 1
    lenr = r - q

    L = [0 for _ in range(lenl)]
    R = [0 for _ in range(lenr)]
    for i in range(lenl):
        L[i] = A[p + i]
    L.append(sys.maxsize)
    
    for i in range(lenr):
        R[i] = A[q + i + 1]
    R.append(sys.maxsize)
    
    left_index, right_index = 0,0
    for i in range(p,r + 1):
        if L[left_index] <= R[right_index]:
            A[i] = L[left_index]
            left_index = left_index + 1
        else:
            A[i] = R[right_index]
            right_index = right_index+1

def MergeSort(A,p,r):
    """
    Merge sort
    """
    if p < r:
        q = (p + r) // 2
        MergeSort(A,p,q)
        MergeSort(A,q + 1,r)
        Merge(A,p,q,r)


def Partition(A,p,r):
    """
    
    """
    x = A[r]
    small_index = p
    for i in range(p,r):
        if A[i] <=  x:
            A[small_index],A[i] = A[i],A[small_index]
            small_index += 1
    A[small_index],A[r] = A[r],A[small_index]
    
    return small_index + 1


def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,q,r)
        QuickSort(A,p,q)
        QuickSort(A,q + 1,r)



def test_merge():
    A = [5,6,7,8,1,2,3,4]
    MergeSort(A,0,7)
    print(A)

def test_quicksort():
    A = [5,6,7,8,1,2,3,4]
    QuickSort(A,0,7)
    print(A)

if __name__ == "__main__":
    test_merge()

