//Bubble sort Algorithm

#include<vector>
#include<iostream>
 using namespace std;

void bubbleSort(int numElements, vector<int>& array, CppAnalyser& analyser)
{
    analyser.startTimer();
    analyser.trackSpace(array);
    
    int min;

    //Traversing the array for sorting
    for(int i = 0; i < numElements; i++)
    {
        analyser.iterate();
        for(int j = 0; j < numElements-i-1; j++)
        {
            //Swapping adjacent elements if the first element is heavier than the second
            if(analyser.comparegt(array[j], array[j+1]))
            {
                analyser.swap(array[j], array[j+1]);
            }
        }
        
    }
    analyser.endTimer();
}