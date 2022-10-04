// Heap Sort Algorithm
#include <vector>
#include <iostream>

using namespace std;

class BinHeap {
    public:
    vector<int> heapList;
    int currentSize;
    CppAnalyser* analyser;

    BinHeap(CppAnalyser& cppAnalyser) {
        currentSize = 0;
        analyser = &cppAnalyser;
    }

    void buildHeap(vector<int>& array) {
        int i = array.size() / 2;
        currentSize = array.size();
        heapList = array;
        heapList.insert(heapList.begin(), 0);
        while(i > 0) {
            percDown(i);
            i--;
        }
    }

    void percDown(int i) {
        while((i * 2) <= currentSize) {
            int mc = maxChild(i);

            if(analyser->comparelt(heapList[i], heapList[mc])) {
                analyser->swap(heapList[i], heapList[mc]);
            }
            i = mc;
        }
    }

    int maxChild(int i) {
        if(i * 2 + 1 > currentSize) return i * 2;
        else {
            if(analyser->comparegt(heapList[i*2], heapList[i*2 + 1])) return i*2;
            else return i*2 + 1;
        }
    }
};

void heapSort(int numElements, vector<int>& array, CppAnalyser &analyser) {
    analyser.startTimer();
    analyser.trackSpace(array);

    BinHeap binHeap = BinHeap(analyser);
    binHeap.buildHeap(array);

    int n = array.size();
    for(int i = n - 1; i>=0; i--) {
        analyser.iterate();
        analyser.swap(binHeap.heapList[0 + 1], binHeap.heapList[i + 1]);
        binHeap.currentSize--;
        binHeap.percDown(0+1);
    }

    for(int i = 0; i<(int)array.size(); i++) {
        array[i] = binHeap.heapList[i+1];
    }

    analyser.endTimer();
}