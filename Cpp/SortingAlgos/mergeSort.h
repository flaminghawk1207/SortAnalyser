#include <vector>

using namespace std;
void mergeSort(int numElements, vector<int>& array, CppAnalyser& analyser) {
    analyser.startTimer();
    sort(array.begin(), array.end());
    analyser.endTimer();
    return;
}