#Median picked pivot for quick sort

def quickSort(ar):

    #Base case
    if len(ar) <= 1:
        return ar

    #A middle element as a pivot
    else:
        mid = len(ar)//2
        pivot = ar[mid]

        # key element is used to break the array
        # in half according to their value
        smaller,greater = [], []

        #Put greater elements in greater list,
        #Smaller elements into smaller list,
        #compare positions to decided where to put
        for indx, val in enumerate(ar):
            if indx != mid:
                if val < pivot:
                    smaller.append(val)
                elif val > pivot:
                    greater.append(val)

                #If value is same, then considering
                #position to decide the list.
                else:
                    if indx < mid:
                        smaller.append(val)
                    else:
                        greater.append(val)
        return quickSort(smaller) + [pivot] + quickSort(greater)

ar = [10, 7, 8, 9, 1, 5, 11, 10]
sortedAr = quickSort(ar)
print(sortedAr)

# Pick last element as pivot

# newSort(arr[], low, high){
#     if (low < high){
#         pi = parition(arr, low, high)

#         newSort(arr, low, pi - 1)
#         newSort(arr, pi + 1, high)
#     }
# }

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [10, 88, 15, 10, 20, 21]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is: ")
for i in range(n):
    print("%d" %arr[i]),

