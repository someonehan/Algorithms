


def heapfy(A, heapsize, index):
    """

    """
    lindex = 2 * index + 1
    rindex = lindex + 1

    largest = index
    if lindex < heapsize and A[lindex] > A[index]:
        largest = lindex

    if rindex < heapsize and A[rindex] > A[largest]:
        largest = rindex

    if largest != index:
        A[largest],A[index] = A[index],A[largest]
        heapfy(A, heapsize, largest)


def build_heap(A):
    """

    """
    for i in range(len(A) // 2, -1,-1):
        heapfy(A,len(A),i)


def heap_sort(A):
    """

    """
    build_heap(A)

    n = len(A)
    
    for i in range(n -1,-1,-1):
        A[0],A[i] = A[i],A[0]
        heapfy(A,i,0)

def test_heapsort():
    l = [2,3,5,2,5,7,6,3,2]
    heap_sort(l)
    print(l)

if __name__ == "__main__":
    test_heapsort()
