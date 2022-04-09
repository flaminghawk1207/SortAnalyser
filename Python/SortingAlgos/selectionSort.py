def selectionSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)
    for i in range(numElements):
        analyser.iterate()
        min = i
        for j in range(i+1, numElements):
            if(analyser.comparelt(array[j], array[min])):
                min = j
        array[i], array[min] = analyser.swap(array[i], array[min])
    analyser.endTimer()