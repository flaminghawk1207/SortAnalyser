# Insertion Sort Algorithm
def insertionSort(numElements, array, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)
    
    # Traveresing the array for Sorting
    for index in range(numElements):

        key = array[index]
        j = index - 1

        # Comparing the array elements with key value
        while ((not analyser.comparelt(j,0)) and analyser.comparegt(array[j],key)):
            analyser.iterate()
            # Shifting the array elements to one position ahead
            array[j+1],array[j] = analyser.swap(array[j+1],array[j])

            j = j - 1
    
        # Replacing the array element with the key value
        array[j+1], key = analyser.swap(array[j + 1], key)

    analyser.endTimer()
