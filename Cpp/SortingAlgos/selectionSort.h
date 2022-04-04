#include<vector>
#include<iostream>
 using namespace std;

void selectionSort(int numElements, vector<int>& array, CppAnalyser& analyser)
{
    analyser.startTimer();
    int min;
    for(int i=0;i<numElements;i++)
    {
        min=i;
        for(int j=i+1;j<numElements;j++)
        {
            analyser.iterate();
            if(analyser.comparelt(array[j],array[min]))
            {
                min=j;
            }
        }
        analyser.swap(array[i],array[min]);
    }
    analyser.endTimer();
}