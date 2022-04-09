#include<vector>
#include<iostream>
 using namespace std;

void selectionSort(int numElements, vector<int>& array, CppAnalyser& analyser)
{
    analyser.startTimer();
    analyser.trackSpace(array);
    int min;
    for(int i = 0; i < numElements; i++)
    {
        analyser.iterate();
        min=i;
        for(int j = i+1;j < numElements; j++)
        {
            if(analyser.comparelt(array[j], array[min]))
            {
                min=j;
            }
        }
        analyser.swap(array[i], array[min]);
    }
    analyser.endTimer();
}