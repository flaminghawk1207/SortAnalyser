from SortingAlgos.insertionSort import insertionSort
# Quick Sorting Algorithm
def partitionPivotSelection(array: list, start: int, end: int,analyser):

    # Setting the pivot point
    pivot = array[end]
    
    if end-start+1 >= 3:
        pivots = [
            [array[start + 0], start+0],
            [array[start + 1], start+1],
            [array[start + 2], start+2],
        ]
        
        if pivots[1][0] < pivots[0][0]:
            analyser.swap(pivot, pivot)
            pivots[0], pivots[1] = pivots[1], pivots[0]
        
        if pivots[2][0] < pivots[1][0]:
            analyser.swap(pivot, pivot)
            pivots[1], pivots[2] = pivots[2], pivots[1]
        
        if pivots[1][0] < pivots[0][0]:
            analyser.swap(pivot, pivot)
            pivots[0], pivots[1] = pivots[1], pivots[0]        

        pivot, pivotIndex = pivots[1]
        array[pivotIndex], array[end] = analyser.swap(array[pivotIndex], array[end])

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

def doQuickSortPivotSelection(array: list, start: int, end: int,analyser):
    if(analyser.comparelt(start,end)):
        # Partitioning The Array
        partition_val = partitionPivotSelection(array,start,end,analyser)
        # Quick Sorting the array indexing from start to (partition index value - 1)
        doQuickSortPivotSelection(array,start,partition_val-1,analyser)
        # Quick Sorting the array indexing from (partition index value + 1) to end
        doQuickSortPivotSelection(array, partition_val+1, end,analyser)

def quickSortPivotSelection(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)
    doQuickSortPivotSelection(array, 0, numElements-1, analyser)
    analyser.endTimer()