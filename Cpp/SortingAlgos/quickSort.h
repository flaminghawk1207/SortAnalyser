// Quick Sorting Algorithm
#include <vector>
#include <iostream>

using namespace std;

int partition(vector<int>& array, int start, int end, CppAnalyser& analyser) {

    // Setting the pivot point
    int pivot = array[end];
    int i = start - 1;
    // Iterating the loop for Sorting
    for(int j = start; j < end; j++) {
        analyser.iterate();
        if(!analyser.comparegt(array[j], pivot)) {
            i++;
            // Swaping the array elements
            analyser.swap(array[i], array[j]);
        }
    }

    // Swaping the array element and the pivot value
    analyser.swap(array[i+1], array[end]);
    // Returning the partition index value
    return i+1;
}

void doQuickSort(vector<int>& array, int start, int end, CppAnalyser& analyser) {
    if(analyser.comparelt(start, end)) {
        // Partitioning The Array
        int partition_val = partition(array, start, end, analyser);
        // Quick Sorting the array indexing from start to (partition index value - 1)
        doQuickSort(array, start, partition_val - 1, analyser);
        // Quick Sorting the array indexing from (partition index value + 1) to end
        doQuickSort(array, partition_val + 1, end, analyser);
    }
}

void quickSort(int numElements, vector<int>& array, CppAnalyser& analyser) {
    analyser.startTimer();
    analyser.trackSpace(array);
    doQuickSort(array, 0, numElements-1, analyser);
    analyser.endTimer();
}