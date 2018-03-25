import math
import sys

def dist(cityOne, cityTwo):
    dx = cityOne['x'] - cityTwo['x']
    dy = cityOne['y'] - cityTwo['y']
    dxSq = math.pow(dx, 2)
    dySq = math.pow(dy, 2)
    return int(round(math.sqrt(dxSq + dySq)))


# merges two subarrays of prqu
# First subarray is pQueue[1..m]
# Second subarray is pQueue[m+1..r]
def merge(pQueue, key, low, high, mid):
    i = low
    j = mid + 1
    temp = []
    # Merge the two halves into temp
    while i <= mid and j <= high:
        if key[pQueue[i]] < key[pQueue[j]]:
            temp.append(pQueue[i])
            i += 1
        else:
            temp.append(pQueue[j])
            j += 1
    # Push all the remaining values from i to mid into temp
    while i <= mid:
        temp.append(pQueue[i])
        i += 1
    # Push all the remaining values from j to high into temp
    while j <= high:
        temp.append(pQueue[j])
        j += 1

    for i in range(low, high+1):
        pQueue[i] = temp[i-low]
def mergeSort(pQueue, cost, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(pQueue, cost, low, mid) # sort first half
        mergeSort(pQueue, cost, mid+1, high) # sort second half
        merge(pQueue, cost, low, high, mid)


def MST_Prim(adjMatrix):
    key = [sys.maxsize for x in range(len(adjMatrix))] # populates a list from 0 to len(cities) with int max
    parent = [None for x in range(len(adjMatrix))]# populates a list from 0 to len(cities) all with None
    prqu = [x for x in range(len(adjMatrix))]   # populates a list from 0 to len(cities) with numbers 0 to len(cities)
    key[0] = 0
    mergeSort(prqu, key, 0, len(prqu) - 1)

    while len(prqu) > 0:
        u = prqu.pop(0)
        for v in [v for v in prqu if adjMatrix[u][v] < key[v]]:
            parent[v] = u   # update how we got to vertex v (from vertex u)
            key[v] = adjMatrix[u][v]
            mergeSort(prqu, key, 0, len(prqu) - 1)
    return parent

def mstToAdjList(adjMatrix, mst):
<<<<<<< HEAD
    adjList = {}
    # for j in range(1, len(adjMatrix) - 1):
    #     if j in mst:
    #         print(j, ' ', mst[j])
    #         # adjList[mst[j]].append({j: adjMatrix[j][mst[j]]})
    #     else:
    #         adjList[mst[j]] = {j: adjMatrix[j][mst[j]]}
    #     print('j = ', j, ' mst[j] = ', mst[j], ' ', adjMatrix[j][mst[j]])
    # print(adjList[1])
    # return adjList
    for i in range(0, len(adjMatrix)): # loop through all cities from 0 to len(adjMatrix)
        adjV = {} #
        for j in [j for j in range(0, len(mst)) if i == mst[j]]:
            adjV[j] = adjMatrix[i][j] # key = city 0 ... len(mst): value = distance from i to j
            print('i = ', i, ' j = ', j, ' ', adjV[j])
        adjList[i] = adjV    # key = city 0 ... len(mst): value: [(key) != adjList[i] && key = city 0 ... len(mst): value = distance from i to j]
=======
    adjList = []
    for i in range(1, len(mst)):
        adjList.append({mst[i]: {i: adjMatrix[i][mst[i]]}})
>>>>>>> 5bc13ce4744379c1ccc2b027b55a00a6c2a572b3
    return adjList
    print(adjList[1][0])
    # stack = []
    # stack.append(mst[0])
    # while len(stack) != 0:
    #     if stack[len(stack) - 1] in mst:
    #         stack.append(mst.index(stack[len(stack) - 1]))
    #     else:
    #         stack.pop()
    # adjList = {}
    # for i in range(0, len(adjMatrix)): # loop through all cities
    #     adjV = {}
    #     for j in range(0, len(mst)): # loop through all parent data
    #         if i == mst[j]:
    #             adjV[j] = adjMatrix[i][j]
    #     adjList[i] = adjV
    # return adjList

def dfs(adjList):
    vstd = []
    stack = []
    stack.append(0)
    #	print (stack)

    while (len(stack) > 0):
        u = stack.pop()
        if not (u in vstd):
            vstd.append(u)
            auxStack = []
            for eachAdj in sorted(adjList[u].items(), key=lambda x: x[1], reverse=True):
                v = eachAdj[0]
                if not (v in vstd):
                    auxStack.append(v)
            while len(auxStack) > 0:
                stack.append(auxStack.pop(0))
    #			print (stack)

    return vstd

def printDistances(distMatrix):
    print('    ', end='')
    for i in range(len(distMatrix)):
        print('{:6}'.format(i), end='')
    print()
    for row in range(len(distMatrix)):
        print('{:4}'.format(row), end='')
        for dist in distMatrix[row]:
            print('{:6}'.format(dist), end='')
        print()
# -----------------------------------------------------------------------------
def main():
    cities = []
    visited_cities = []
    fileName = 'tsp_example_1.txt'
    inputFile = open(fileName, 'r')
    # get cities from input file into a list
    cities = []
    for line in inputFile:
        city = line.split()
        cities.append({'id': int(city[0]), 'x': int(city[1]), 'y': int(city[2])})
    inputFile.close()
    #
    # print(cities)

    # init adjacency matrix for graph (every city connected to every other city)
    adjMatrix = [[0 for x in range(len(cities))] for y in range(len(cities))]
    for u in range(0, len(cities)):
        for v in range(u + 1, len(cities)):
            ij = dist(cities[u], cities[v])
            adjMatrix[u][v] = ij
            adjMatrix[v][u] = ij

    printDistances(adjMatrix)

    # create minimum spanning tree (MST) using Prim's algorithm which is
    # faster on dense graphs than Kruskal's algorithm - I consider my graph
    # to be dense because every vertex (city) is connected to every other
    mst = MST_Prim(adjMatrix)
    print(mst)
    # mst = kruskalsAlg(adjMatrix)
    #	print (mst)

    # convert mst into adjacencyList
    adjList = mstToAdjList(adjMatrix, mst)
    print(adjList)
    #	print (adjList)

    # get DFS discovered order
<<<<<<< HEAD
    disc = dfs(adjList)
    #	print (disc)

    # # calc the total distance from city 0 to 1 to 2 to n-1 to n to 0
    totalDist = 0
    iterCities = iter(disc) # return an iterator for the given object
    prevCity = cities[disc[0]]
    next(iterCities)  # skip the very first city
    for eachItem in iterCities:
        eachCity = cities[eachItem]
        # get distance to eachCity from the prevCity
        addDist = dist(eachCity, prevCity)
        totalDist = totalDist + addDist
        prevCity = eachCity

    # get distance from last city back to first city
    addDist = dist(prevCity, cities[disc[0]])
    totalDist = totalDist + addDist

    # write output to file
    # outFil.write(str(totalDist) + '\n')
    print(totalDist)
    iterCities = iter(disc)
    for eachCity in iterCities:
        print(eachCity)
=======
    # disc = dfs(adjList)
    # #	print (disc)
    #
    # # calc the total distance from city 0 to 1 to 2 to n-1 to n to 0
    # totalDist = 0
    # iterCities = iter(disc) # return an iterator for the given object
    # prevCity = cities[disc[0]]
    # next(iterCities)  # skip the very first city
    # for eachItem in iterCities:
    #     eachCity = cities[eachItem]
    #     # get distance to eachCity from the prevCity
    #     addDist = dist(eachCity, prevCity)
    #     totalDist = totalDist + addDist
    #     prevCity = eachCity
    #
    # # get distance from last city back to first city
    # addDist = dist(prevCity, cities[disc[0]])
    # totalDist = totalDist + addDist
    #
    # # write output to file
    # # outFil.write(str(totalDist) + '\n')
    # print(totalDist)
    # iterCities = iter(disc)
    # for eachCity in iterCities:
    #     print(eachCity)
>>>>>>> 5bc13ce4744379c1ccc2b027b55a00a6c2a572b3

if __name__ == "__main__":
    main()
