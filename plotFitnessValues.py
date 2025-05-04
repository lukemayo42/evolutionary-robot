import numpy as np
import matplotlib.pyplot as plt

def plot():
    dataA = np.load("dataA.npy")
    dataB = np.load("dataB.npy")
    mA = np.mean(dataA, axis = 0)
    mB = np.mean(dataB, axis = 0)
    rowA = find_best_fitness(dataA)
    rowB = find_best_fitness(dataB)
    stdA = np.std(dataA, axis = 0)
    stdB = np.std(dataB, axis = 0)
    x = np.arange(dataA.shape[1])
    plt.plot(mA, color = 'blue')
    plt.plot(mB, color = 'red')
    plt.plot(dataA[rowA, :], linestyle='dashed', color='blue')
    plt.plot(dataB[rowB, :], linestyle='dashed', color='red')
    plt.fill_between(x, mA - stdA, mA + stdA, color = 'blue', alpha = 0.2)
    plt.fill_between(x, mB - stdB, mB + stdB, color = 'red', alpha = 0.2)
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness")
    plt.title("Average Fitness over Generations")
    plt.legend(["A", "B", "Best Solution from A", "Best Solution from B"])
    plt.show()

def find_best_fitness(arr):
    # get final column
    last = arr[:, -1]
    best = 0
    best_ind = 0
    for i in range(len(last)):
        if last[i] < best:
            best = last[i]
            best_ind = i
    return best_ind

plot()


