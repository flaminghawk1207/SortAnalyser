//Selection Sort Algorithm

#include<vector>
#include<iostream>
 using namespace std;

void selectionSort(int numElements, vector<int>& array, CppAnalyser& analyser)
{
    analyser.startTimer();
    analyser.trackSpace(array);
    int min;

    //Traversing the array for sorting 

    for(int i = 0; i < numElements; i++)
    {
        min=i;

        //Traversing through the array and finding the index of the smallest array in the unsorted part

        for(int j = i+1;j < numElements; j++)
        {
            analyser.iterate();
            if(analyser.comparelt(array[j], array[min]))
            {
                min=j;
            }
        }

        //Swapping the current element and the smallest element in the unsorted array
        analyser.swap(array[i], array[min]);
    }
    analyser.endTimer();
}