# Quick Sorting Algorithm
def partition(array: list,start: int,end: int,analyser):
    # Setting the pivot point
    pivot = array[end]
    i = start-1    
    # Iterating the loop for Sorting
    for j in range(start,end):
        analyser.iterate()
        if(not analyser.comparegt(array[j],pivot)):
            i+=1
            # Swaping the array elements
            array[i],array[j] = analyser.swap(array[i],array[j])
    # Swaping the array element and the pivot value
    array[i+1],array[end] = analyser.swap(array[i+1],array[end])
    # Returning the partition index value
    return i+1

def doQuickSort(array: list,start: int,end: int,analyser):
    if(analyser.comparelt(start,end)):
        # Partitioning The Array
        partition_val = partition(array,start,end,analyser)
        # Quick Sorting the array indexing from start to (partition index value - 1)
        doQuickSort(array,start,partition_val-1,analyser)
        # Quick Sorting the array indexing from (partition index value + 1) to end
        doQuickSort(array, partition_val+1, end,analyser)

def quickSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)
    doQuickSort(array, 0, numElements-1, analyser)
    analyser.endTimer()