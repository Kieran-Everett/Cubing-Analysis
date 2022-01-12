import sys
import json
import math
import matplotlib.pyplot as plt
import numpy as np

def getSolveTimes():
    fileToOpen = input('File: ')
    session = input('Session: ')

    if fileToOpen == "":
        fileToOpen = "data/cstimer_export.txt"
        session = "session1"

    try:
        with open(fileToOpen) as file:
            data = file.read()
    except FileNotFoundError:
        print("Error: File does not exist")
        sys.exit()

    data = json.loads(data)
    data = data[session]

    rawTimes = []
    for solve in data:
        rawTimes.append(solve[0][1])
    
    output = []
    for solve in rawTimes:
        x = str(solve)
        x = x[:-3] + '.' + x[-3:] # adding in the decimal place
        x = float(x)
        output.append(x)
    
    return output

def generateRollingAverage(solveTimes):
    averageLength = 50

    averaged = []
    current = [i for i in range(1,averageLength+1)]
    count = 0
    looped = False
    for i in solveTimes:
        if count == averageLength:
            count = 0
            looped = True
        current[count] = i
        if looped == True:
            averaged.append(sum(current)/len(current))
        else:
            averaged.append(30)
        count += 1
    return averaged
        

def graph(solveTimes):

    #longestSolve = math.ceil(max(solveTimes))
    #shortestSolve = math.floor(min(solveTimes))
    #y = []
    #for i in range(shortestSolve, longestSolve+1):
    #    y.append(i)

    plt.plot(solveTimes)
    plt.plot(generateRollingAverage(solveTimes))

    #solveTimes = np.asarray(solveTimes)

    #m, b = np.polyfit(solveTimes, solveTimes, 1)

    #plt.plot(solveTimes, m*solveTimes + b)

    plt.xlabel('Solve number')
    plt.ylabel('Sovlve time')

    plt.title('3x3 Solves')

    plt.show()

def main():
    solveTimes = getSolveTimes()
    graph(solveTimes)

if __name__ == '__main__':
    main()