#include <time.h>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <vector>

using namespace std;

class CppAnalyser {
    private:

        long long int iterations;
        long long int comparisons;
        long long int swaps;
        long long int space;

        clock_t start, end;
        
    public:

        CppAnalyser(): 
            iterations(0), 
            comparisons(0), 
            swaps(0),
            space(0),
            start(0),
            end(0) {}

        // Starts timer (Called at beginning of sort)
        void startTimer() {
            if(start) return;
            start = clock();
        }

        // Stops timer (Called after sort is done)
        void endTimer() {
            end = clock();
        }

        // Counts iterations
        void iterate() {
            iterations++;
        }

        // Counts and performs comparison (less than)
        bool comparelt(int x, int y) {
            comparisons++;
            return x < y;
        }

        // Counts and performs comparison (greater than)
        bool comparegt(int x, int y) {
            comparisons++;
            return x > y;
        }

        // Counts and performs swap
        void swap(int& x, int& y) {
            swaps++;
            std::swap(x, y);
        }

        // Tracks the amount of space used
        void trackSpace(vector<int>& array) {
            space += array.size() * sizeof(int);
        }

        // Un-Track space
        // Used when other algos are used to sort inplace
        // But they track space
        void unTrackSpace(vector<int>& array) {
            space -= array.size() * sizeof(int);
        }

        // Writes the run data to file
        void dump(string name) {
            ofstream fout;
            fout.open(name);

            fout<<"Iterations: "<<iterations<<endl;
            fout<<"Comparisons: "<<comparisons<<endl;
            fout<<"Swaps: "<<swaps<<endl;
            fout<<fixed<<setprecision(10);
            fout<<"Time: "<<double(end-start)/CLOCKS_PER_SEC<<endl;
            fout<<"Space: "<<space<<endl;
        }
};