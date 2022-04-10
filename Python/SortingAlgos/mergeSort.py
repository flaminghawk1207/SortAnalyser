# Merge Sorting Algorithm
def domergeSort(array: list, analyser):
    size = len(array)
    if analyser.comparegt(size,1):
        # Partitioning the array into 2 Parts by the middle value
        middle = size//2
        Left = array[:middle]
        Right = array[middle:]

        analyser.trackSpace(Left)
        analyser.trackSpace(Right)

        # Merge Sortng the First half
        domergeSort(Left,analyser)
        # Merge sorting the second half
        domergeSort(Right,analyser)

        index = 0
        left = 0
        right = 0

        # Comparing and Storing the array elements 
        # in a temperary array in a sorted order
        while left < len(Left) and right < len(Right):
            analyser.iterate()
            if analyser.comparelt(Left[left], Right[right]):
                array[index] = Left[left]
                left += 1
            else:
                array[index] = Right[right]
                right += 1
            index += 1

        # Storing the remaing array elements in first half in that temperary array
        while analyser.comparelt(left, len(Left)):
            analyser.iterate()
            array[index] = Left[left]
            left += 1
            index += 1

        # Storing the remaing array elements in second half in that temperary array
        while analyser.comparelt(right,len(Right)):
            analyser.iterate()
            array[index] = Right[right]
            right += 1
            index += 1

# Calling the merge algorithm and
# Counting the time taken of execution
def mergeSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    domergeSort(array,analyser)
    analyser.endTimer()
