from SortingAlgos.insertionSort import insertionSort
from SortingAlgos.mergeSort import mergeSort
def minlen(n):
	r=0
	while n>=32:
		r|=n&1
		n>>=1
	return n+r


def insertion(array,begin,end,analyser):
	for i in range(begin+1,end+1):
		analyser.iterate()
		j=i
		while analyser.comparegt(j,begin) and analyser.comparelt(array[j],array[j-1]):
			array[j],array[j-1]=analyser.swap(array[j],array[j-1])
			j-=1

def mergeInsertionSort(numElements,array,analyser):
	analyser.startTimer()
	n=len(array)
	m=minlen(n)
	for i in range(0,n,m):
		end=min(i+m-1,n-1)
		insertion(array,i,end,analyser)
	length=m
	mergeSort(numElements,array,analyser)
	analyser.endTimer()