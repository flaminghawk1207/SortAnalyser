from more_itertools import is_sorted
import os, sys
from pyAnalyser import PyAnalyser

from SortingAlgos.bubbleSort import bubbleSort
from SortingAlgos.insertionSort import insertionSort
from SortingAlgos.mergeSort import mergeSort
from SortingAlgos.quickSort import quickSort
from SortingAlgos.selectionSort import selectionSort

# To add new algorithms, add a new entry in this dictionary
# Key - Algorithm name, will be recognised from commandline
# Value - Function name
# Don't forget to import the sorting function
FUNCTIONS_DICT = {
    "bubbleSort" : bubbleSort,
    "insertionSort" : insertionSort,
    "mergeSort" : mergeSort,
    "quickSort" : quickSort,
    "selectionSort" : selectionSort
}

def readArray():
    with open(os.path.join(os.path.dirname(os.getcwd()), 'array.txt'), "r") as f:
        numElements = int(f.readline())
        array = [int(x) for x in f.readline().split()]
    return numElements, array

def runAnalysis(sortingFunction):

    # Check if the sorting function is available
    if sortingFunction not in FUNCTIONS_DICT:
        raise AttributeError("Sorting function not available")

    # Read array from file
    numElements, array = readArray()

    # Create analyser object
    analyser = PyAnalyser()

    # Call the sorting function
    FUNCTIONS_DICT[sortingFunction](numElements, array, analyser)
    
    print(sortingFunction)
    # Check if array is sorted
    assert is_sorted(array), "Output array not sorted"

    # Write data to file
    analyser.dump(os.path.join("SortingAlgos", "data", sortingFunction + ".txt"))

if __name__ == "__main__":

    assert len(sys.argv) == 2, "Invalid number of arguments"
    runAnalysis(sys.argv[1])