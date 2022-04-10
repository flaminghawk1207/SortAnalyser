#Selection Sort Algorithm

def selectionSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)

    #Traversing the array for sorting 

    for i in range(numElements):
        min = i

        #Traversing through the array and finding the index of the smallest array in the unsorted part

        for j in range(i+1, numElements):
            analyser.iterate()
            if(analyser.comparelt(array[j], array[min])):
                min = j

        #Swapping the current element and the smallest element in the unsorted array       
        
        array[i], array[min] = analyser.swap(array[i], array[min])
    analyser.endTimer()