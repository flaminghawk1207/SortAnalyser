def bubbleSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)
    for i in range(numElements):
        analyser.iterate()
        for j in range(numElements-i-1):
            if(analyser.comparegt(array[j], array[j+1])):
                array[j+1], array[j] = analyser.swap(array[j+1], array[j])
    analyser.endTimer()