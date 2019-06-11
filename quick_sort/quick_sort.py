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