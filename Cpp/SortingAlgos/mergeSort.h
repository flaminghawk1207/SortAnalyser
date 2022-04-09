#include <vector>
using namespace std;
void merge(vector<int>& array, int start, int mid, int end, CppAnalyser& analyser)
{
    analyser.iterate();

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
    
    
    while(idxl < l && idxr < r)
    {
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
    
    while(idxl < l)
    {
        array[idxm]=larray[idxl];
        idxl++;
        idxm++;
    }
    
    while(idxr < r)
    {
        array[idxm]=rarray[idxr];
        idxr++;
        idxm++;
    }
}

void doMergeSort(vector<int>& array, int start, int end, CppAnalyser& analyser)
{
    if(start>=end) //compare greater
    {
        return;
    }
    else
    {
        int mid=start + (end-start)/2;
        doMergeSort(array,start,mid, analyser);
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
