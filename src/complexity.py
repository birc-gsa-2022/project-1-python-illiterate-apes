import matplotlib.pyplot as plt
import numpy as np
import lin
import naive
import timeit



 


def main():
    
    #Best Cases
    
    #NAIVE

    #Read length variance for naive
    genome = [0,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*20]
    reads = [[0,i * "baaaa"] for i in range(1,20,1)]
    runtimes = calculateRuntimesReads(reads, genome, "naive") # plt.title("naive alg runtime variance according to variance in read length - Best Case")
    x = np.array([i[0] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "naive alg runtime variance according to variance in read length - Best Case")

    #Genome length variance for naive
    read = [0,"baaaaaaaaaaaaaaa"]
    genomes = [[0,i * "aaaaaaaaaaaaaaaa"] for i in range(1,6000,500)]
    runtimes = calculateRuntimesGenomes(read, genomes, "naive")#plt.title("naive alg runtime variance according to variance in genome length - Best Case")
    x = np.array([i[1] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "naive alg runtime variance according to variance in genome length - Best Case")

    #Combined Genome and Read length variance for naive
    reads = [[0,i * "baaaa"] for i in range(1,1000,50)]
    genomes = [[0,i * "aaaaaaaaaaaaaaaa"] for i in range(1,1000,50)]
    runtimes = calculateRuntimesCombined(reads, genomes, "naive")
    x = np.array([i for i in range(len(runtimes))])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "naive alg runtime variance according to variance in genome and read length - Best Case")
    

    #LINEAR
    
    #Read length variance for linear
    genome = [0,"ababaabcabacacb"*20]
    reads = [[0,i * "ababa"] for i in range(1,20,1)]
    runtimes = calculateRuntimesReads(reads, genome, "linear")
    x = np.array([i[0] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in read length - Best Case")

    #Genome length variance for linear
    read = [0,"ababa"]
    genomes = [[0,i * "ababaabcabacacb"] for i in range(1,6000,500)]
    runtimes = calculateRuntimesGenomes(read, genomes, "linear")
    x = np.array([i[1] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in genome length - Best Case")

    #Combined Genome and Read length variance for linear

    reads = [[0,i * "ababa"] for i in range(1,1000,50)]
    genomes = [[0,i * "ababaabcabacacb"] for i in range(1,1000,50)]
    runtimes = calculateRuntimesCombined(reads, genomes, "linear")
    x = np.array([i for i in range(len(runtimes))])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in genome and read length - Best Case")

    #WORST CASES
    #Read length variance for naive
    genome = [0,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*20]
    reads = [[0,i * "aaaaa"] for i in range(1,20,1)]
    
    
    runtimes = calculateRuntimesReads(reads, genome, "naive")
    x = np.array([i[0] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "naive alg runtime variance according to variance in read length - Worst Case")

    #Genome length variance for naive
    read = [0,"aaaaaaaaaaaaaaaa"]
    genomes = [[0,i * "aaaaaaaaaaaaaaaa"] for i in range(1,6000,500)]
    runtimes = calculateRuntimesGenomes(read, genomes, "naive")
    x = np.array([i[1] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "naive alg runtime variance according to variance in genome length - Worst Case")

    #Combined Genome and Read length variance for naive

    reads = [[0,i * "aaaaa"] for i in range(1,1000,50)]
    genomes = [[0,i * "aaaaaaaaaaaaaaaa"] for i in range(1,1000,50)]
    runtimes = calculateRuntimesCombined(reads, genomes, "naive")
    x = np.array([i for i in range(len(runtimes))])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 2, "naive alg runtime variance according to variance in genome and read length - Worst Case")


    #LINEAR

    #Read length variance for linear
    genome = [0,"aaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaab"*20]
    reads = [[0,i * "aaaaaaaaaaaaaaaaa"] for i in range(1,20,1)]
    runtimes = calculateRuntimesReads(reads, genome, "linear")
    x = np.array([i[0] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in read length - Worst Case")

    #Genome length variance for linear
    read = [0,"aaaaaaaaaaaaaaaaa"]
    genomes = [[0,i * "aaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaab"] for i in range(1,6000,500)]
    runtimes = calculateRuntimesGenomes(read, genomes, "linear")
    x = np.array([i[1] for i in runtimes])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in genome length - Worst Case")

    #Combined Genome and Read length variance for linear
    reads = [[0,i * "aaaaaaaaaaaaaaaaa"] for i in range(1,1000,50)]
    genomes = [[0,i * "aaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaabaaaaaaaaaaab"] for i in range(1,1000,50)]
    runtimes = calculateRuntimesCombined(reads, genomes, "linear")
    x = np.array([i for i in range(len(runtimes))])
    y = np.array([i[2] for i in runtimes])
    plotLinearRegressionRuntime(x,y, 1, "linear alg runtime variance according to variance in genome and read length - Worst Case")
 
def plotLinearRegressionRuntime(x: np.ndarray, y: np.ndarray, expDeg: int, title: str):
    """
    plots runtimes in a scatterplot and fits a regression line
    """
    plt.title(title)
    if expDeg == 1:
        m, b = np.polyfit(x,y,deg=1)
        plt.plot(x,m*x+b, color = "red")
    else:
        n, m, b = np.polyfit(x,y,deg=2)
        plt.plot(x, n*pow(x,2)+m*x+b, color = "red")
    
    plt.scatter(x,y)
    plt.show()


def calculateRuntimesCombined(reads: list[str], genome: str, alg: str) -> list[float]:
    """
    calculates runtimes for different reads against different Genomes
    """
    runtimes = []
    for i in range(len(reads)):

        if alg == "naive":
            start = timeit.default_timer()
            naive.naive(reads[i],genome[i])
            stop = timeit.default_timer()
        if alg == "linear":
            start = timeit.default_timer()
            lin.linear(reads[i],genome[i])
            stop = timeit.default_timer()

        
        runtimes.append([len(reads[i][1]), len(genome[i][1]), stop - start])
    return runtimes

def calculateRuntimesReads(reads: list[str], genome: str, alg: str) -> list[float]:
    """
    calculates runtimes for different reads against a genome
    """
    runtimes = []
    for read in reads:

        if alg == "naive":
            start = timeit.default_timer()
            naive.naive(read,genome)
            stop = timeit.default_timer()
        if alg == "linear":
            start = timeit.default_timer()
            lin.linear(read,genome)
            stop = timeit.default_timer()

        
        runtimes.append([len(read[1]), len(genome), stop - start])
    return runtimes

def calculateRuntimesGenomes(read: str, genomes: list[str],alg: str) -> list[float]:
    """
    calculates runtimes for a read against different genomes
    """
    runtimes = []
    for genome in genomes:
        start = timeit.default_timer()

        if alg == "naive":
            naive.naive(read,genome)
        if alg == "linear":
            lin.linear(read,genome)

        stop = timeit.default_timer()
        runtimes.append([len(read), len(genome[1]), stop - start])
    return runtimes
    




if __name__ == "__main__":
    main()
