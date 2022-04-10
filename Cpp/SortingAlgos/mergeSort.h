//Merge Sort Algorithm

#include <vector>
using namespace std;
void merge(vector<int>& array, int start, int mid, int end, CppAnalyser& analyser)
{

    int l=mid-start+1;
    int r=end-mid;

    vector<int> larray(l), rarray(r);
    analyser.trackSpace(larray);
    analyser.trackSpace(rarray);
    
    for(int i=0;i<l;i++)
    {
        larray[i]=array[start+i];
    }
    for(int i=0;i<r;i++)
    {
        rarray[i]=array[mid+1+i];
    }
    
    int idxl=0, idxr=0, idxm=start;
    
    //Comparing and Storing the array elements in a temperary array in a sorted order

    while(idxl < l && idxr < r)
    {
        analyser.iterate();
        if(!analyser.comparegt(larray[idxl], rarray[idxr]))
        {
            array[idxm]=larray[idxl];
            idxl++;
        }
        else
        {
            array[idxm]=rarray[idxr];
            idxr++;
        }
        idxm++;
    }
    

    //Storing the remaing array elements in first half in that temperary array
    while(idxl < l)
    {
        analyser.iterate();
        array[idxm]=larray[idxl];
        idxl++;
        idxm++;
    }
    

    //Storing the remaing array elements in second half in that temperary array
    while(idxr < r)
    {
        analyser.iterate();
        array[idxm]=rarray[idxr];
        idxr++;
        idxm++;
    }
}

void doMergeSort(vector<int>& array, int start, int end, CppAnalyser& analyser)
{
    if(start>=end)
    {
        return;
    }
    else
    {

        //Partitioning the array into 2 Parts by the middle value

        int mid=start + (end-start)/2;

        //Merge Sortng the First half
        doMergeSort(array,start,mid, analyser);

        //Merge Sortng the Second half
        doMergeSort(array,mid+1,end, analyser);
        merge(array,start,mid,end, analyser);
    }
}


void mergeSort(int numElements, vector<int>& array, CppAnalyser& analyser) {
    analyser.startTimer();
    analyser.trackSpace(array);
    doMergeSort(array, 0, numElements-1, analyser);
    analyser.endTimer();
    return;
}
