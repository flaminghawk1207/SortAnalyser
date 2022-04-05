import numpy as np
import matplotlib.pyplot as plt
import os, json

LANGS = {
    "Cpp" : "g++ cppSorter.cpp -o cppSorter && cppSorter {0}",
    "Python" : "python pySorter.py {0}"
}

ALGORITHMS = ["quickSort"]

INPUT_SIZES = [10**i for i in range(8)]

QUANTITIES = [ "Comparisons", "Swaps", "Iterations", "Time", "Space"]

# Dictionary with algos as key, another dictionary as value
    # dictionary with inputsize as key, another dictionary as value
        # dictionary with language as key, another dictionary as value
            # dictionary with quantity as key, measurements as value
RUN_DATA = dict()

def generateArray(inputSize):
    array = np.random.randint(inputSize, size=inputSize)

    with open("array.txt", "w") as f:
        print(inputSize, file=f)
        print(*array, file=f, end="")

def execute(algo, lang):
    os.chdir(lang)
    os.system(LANGS[lang].format(algo))
    os.chdir("..")

def readData(algo, lang):
    path = os.path.join(lang, "SortingAlgos", "data", f"{algo}.txt")
    data = {}
    with open(path, "r") as f:
        
        for line in f:
            quantity, value = line.strip().split(": ")
            data[quantity] = float(value)

    return data

def recordData(inputSize):
    
    for algo in ALGORITHMS:
        if algo not in RUN_DATA:
            RUN_DATA[algo] = {}
        RUN_DATA[algo][inputSize] = {}

        for lang in LANGS:
            RUN_DATA[algo][inputSize][lang] = readData(algo, lang)

def runAnalysis():

    for inputSize in INPUT_SIZES:
        generateArray(inputSize)
        print(f"Size {inputSize}")
        for algo in ALGORITHMS:

            print(f"Analysing {algo}")
            for lang in LANGS:
                print(f"Running in {lang}")
                execute(algo, lang)

        recordData(inputSize)

    print(RUN_DATA)

def plotQuantity(quantity):

    for lang in LANGS:
        for algo in ALGORITHMS:
            measures = [RUN_DATA[algo][inputSize][lang][quantity] for inputSize in INPUT_SIZES]
            plt.plot(INPUT_SIZES, measures, markersize = 25)

        plt.savefig(os.path.join("Plots", "_".join([quantity, lang])))
        plt.clf()


def plot():
    for quantity in QUANTITIES:
        plotQuantity(quantity)

if __name__ == "__main__":
    runAnalysis()
    plot()
    with open("runData.json", "w") as f:
        json.dump(RUN_DATA, f)