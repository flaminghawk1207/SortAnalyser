import time

class PyAnalyser:
    def __init__(self):
        self.__iterations = 0
        self.__comparisons = 0
        self.__swaps = 0
        self.__start = None
        self.__end = None

    # Starts timer (Called at beginning of sort)
    def startTimer(self):
        self.__start = time.time()

    # Stops timer (Called after sort is done)
    def endTimer(self):
        self.__end = time.time()

    # Counts iterations
    def iterate(self):
        self.__iterations += 1

    # Counts and performs comparison (less than)
    def comparelt(self, x, y):
        self.__comparisons += 1
        return x < y

    # Counts and performs comparison (greater than)
    def comparegt(self, x, y):
        self.__comparisons += 1
        return x > y

    # Counts and performs swap
    def swap(self, x, y):
        self.__swaps += 1
        return y, x

    # Writes the run data to file
    def dump(self, name):

        with open(name, 'w') as f:
            print(f"Iterations: {self.__iterations}", file=f)
            print(f"Comparisons: {self.__comparisons}", file=f)
            print(f"Swaps: {self.__swaps}", file=f)
            print(f"Time: {round(self.__end - self.__start, 10)}", file=f)