def hyperid_sort ( arr , threshold):

    if len(arr) <= threshold :
        return  insertion_sort(arr)
    else :
       return mergeSort(arr)




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSort(arr):
    _mergeSort(arr,0,len(arr)-1)
    return arr
def _mergeSort(arr,l,h):
    if(l<h):
        m=(l+h)//2
        _mergeSort(arr,l,m)
        _mergeSort(arr,m+1,h)

        merge(arr,l,h)

def merge(arr,l,h):
    newarr= []
    m=(l+h)//2
    i = l
    j = m+1
    k=l
    while(i<=m and j<=h):
        if(arr[i]<=arr[j]):
            newarr.append(arr[i])
            i+=1
        else:
            newarr.append(arr[j])
            j+=1
        k+=1
    while(i<=m):
        newarr.append(arr[i])
        i+=1
        k+=1
    while(j<=h):
        newarr.append(arr[j])
        j+=1
        k+=1
    for i in range(len(newarr)):
        arr[l + i] = newarr[i]

    return  arr

arr = [5, 2, 8, 3, 9, 1]
threshold = 5
sorted_arr = hyperid_sort(arr, threshold)
print("Sorted array:", sorted_arr)