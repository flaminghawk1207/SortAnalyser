#heap sort algorithm
class maxHeap:
	def __init__(self, analyser):
		self.heapList = []
		self.currentSize = 0
		self.analyser = analyser

	def buildHeap(self, array):
		i = len(array) // 2
		self.currentSize = len(array)
		self.heapList = [0] + array[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.maxChild(i)
			if self.analyser.comparelt(self.heapList[i], self.heapList[mc]):
				self.heapList[i], self.heapList[mc] = self.analyser.swap(self.heapList[i], self.heapList[mc])
			i = mc

	def maxChild(self, i):
		if(2*i +1 > self.currentSize):
			return i*2
		else:
			if(self.analyser.comparegt(self.heapList[i*2], self.heapList[i*2 +1])):
				return i*2
			else:
				return (i*2)+1

	def printHeap(self):
		print(self.heapList)
	
def heapSort(numElements, array, analyser):
	analyser.startTimer()
	analyser.trackSpace(array)
	heaper = maxHeap(analyser)
	heaper.buildHeap(array)

	for i in range(numElements-1, -1, -1):
		analyser.iterate()
		heaper.heapList[i+1], heaper.heapList[0+1] = analyser.swap(heaper.heapList[i+1], heaper.heapList[0+1])
		heaper.currentSize -= 1
		heaper.percDown(0+1)

	for j in range(len(array)):
		array[j] = heaper.heapList[j+1]
	analyser.endTimer()