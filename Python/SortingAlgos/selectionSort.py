def selectionSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    for i in range(numElements):
        min=i
        for j in range(i+1,numElements):
            analyser.iterate()
            if(analyser.comparelt(array[j],array[min])):
                min=j
        array[i],array[min] = analyser.swap(array[i],array[min])
    analyser.endTimer()