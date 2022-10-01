#bucket sort algorithm
from SortingAlgos.insertionSort import insertionSort
def bucketSort(numElements,array,analyser):
	analyser.startTimer()
	analyser.trackSpace(array)
	numofBuckets=10
	bucketed=[]
	for i in range(numofBuckets):
		bucketed.append([])
	for j in range(len(array)):
		index=(numofBuckets*array[j])//(max(array)+1)
		bucketed[index].append(array[j])
	for k in range(numofBuckets):
		insertionSort(len(bucketed[k]),bucketed[k],analyser)
	ind=0
	for i in range(numofBuckets):
		for j in range(len(bucketed[i])):
			array[ind]=bucketed[i][j]
			ind+=1
	analyser.endTimer()