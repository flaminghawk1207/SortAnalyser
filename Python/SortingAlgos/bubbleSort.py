#Bubble sort Algorithm

def bubbleSort(numElements: int, array: list, analyser):
    analyser.startTimer()
    analyser.trackSpace(array)

    #Traversing the array for sorting
    for i in range(numElements):
        for j in range(numElements-i-1):
            analyser.iterate()

            #Swapping adjacent elements if the first element is heavier than the second

            if(analyser.comparegt(array[j], array[j+1])):
                array[j+1], array[j] = analyser.swap(array[j+1], array[j])        
                
    analyser.endTimer()