

def insert_sort(A):
    for i in range(1,len(A)):
        j = i -1
        k = A[i]
        while j >= 0 and A[j] > k:
            A[i] = A[j]
            j = j -1

        A[j + 1] = k


def counting_sort(A, k):
    """counting sort"""

    n = len(A)

    c = [0 for _ in range(k + 1)]
    b = [0 for _ in range(n)]


    for i in range(0, n):
        c[A[i]] = c[A[i]] + 1

    for i in range(1, k + 1):
        c[i] = c[i] + c[i-1]
    
    for j in range(n):
        b[c[A[j]]-1] = A[j]
        c[A[j]] = c[A[j]] - 1  
    return b


def test_insert_sort():
    l = [2,4,3,4,3]
    insert_sort(l)
    print(l)

def test_counting_sort():
    l = [3,5,3,2,35,3]
    l =  counting_sort(l, 35)
    print(l)

if __name__ == "__main__":
    test_counting_sort()
