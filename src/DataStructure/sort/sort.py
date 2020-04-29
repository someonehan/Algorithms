

def insertsort(l):
    for i in range(len(l)):
        tmp = l[i]
        j = i
        while j > 0 and l[j - 1] > tmp:
            l[j] = l[j - 1]
            j -= 1
        l[j] = tmp


def selectsort(l):
    for i in range(len(l)):
        min = l[i]
        k = i
        for j in range(i + 1, len(l)):
            if min > l[j]:
                min = l[j]
                k = j
        l[k] = l[i]
        l[i] = min


def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]



if __name__ == "__main__":
    al = [3,34,54,231,321,23,1,1]
    bubblesort(al)
    print(al)