#heap sort algorithm
class maxHeap:
	def __init__(self,analyser):
		self.temp=[]
		self.size=0
		self.analyser=analyser
	def buildHeap(self,array):
		i=len(array)//2
		self.size=len(array)
		for j in range(len(array)):
			self.temp.append(array[j])
		self.temp.insert(0,0)
		print(i)
		while(i>0):
			self.percDown(i)
			i-=1
		print(self.temp)
	def percDown(self,i):
		while((i*2)<=self.size):
			mc=self.maxChild(i)
			if(self.analyser.comparelt(self.temp[i],self.temp[mc])):
				self.temp[mc],self.temp[i]=self.analyser.swap(self.temp[i],self.temp[mc])
			i=mc
	def maxChild(self,i):
		if(2*i +1 >self.size):
			return i*2
		else:
			if(self.analyser.comparegt(self.temp[i*2],self.temp[i*2 +1])):
				return i*2
			else:
				return (i*2)+1
	def printHeap(self):
		print(self.temp)



	
def heapSort(numElements,array,analyser):
	analyser.startTimer()
	analyser.trackSpace(array)
	heaper=maxHeap(analyser)
	heaper.buildHeap(array)
	print("qwerty")

	n=len(array)
	for i in range(n-1,-1,-1):
		analyser.iterate()
		heaper.temp[0+1],heaper.temp[i+1]=heaper.temp[i+1],heaper.temp[0+1]
		heaper.size-=1
		heaper.percDown(0+1)
	heaper.printHeap()
	for j in range(len(array)):
		array[j]=heaper.temp[j+1]
	analyser.endTimer()


	






	analyser.endTimer()