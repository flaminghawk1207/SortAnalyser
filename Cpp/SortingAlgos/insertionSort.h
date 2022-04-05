// Insertion Sort Algorithm
#include <vector>
#include <iostream>

using namespace std;

void insertionSort( int numElements, vector<int>& array, CppAnalyser &analyser) {

    analyser.startTimer();
    analyser.trackSpace(array);
    
    int key, j;
    // Traveresing the array for Sorting
    for(int index = 0; index < numElements; index++ ) {
        analyser.iterate();
        
        key = array[index];
        j = index - 1;
        
        // Comparing the array elements with key value
        while ((!analyser.comparelt(j,0)) && analyser.comparegt(array[j],key)) {
            analyser.iterate();
        
            // Shifting the array elements to one position ahead
            analyser.swap(array[j + 1], array[j]);
        
            j = j - 1;
        }
        
        // Replacing the array element with the key value
        analyser.swap(array[j + 1], key);
    }
    analyser.endTimer();
} 