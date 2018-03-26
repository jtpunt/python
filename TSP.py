import math
import sys
from collections import OrderedDict

def EuclideanDistance(c1, c2):
    xSquared = math.pow(c1[1] - c2[1], 2)
    ySquared = math.pow(c1[2] - c2[2], 2)
    return int(round(math.sqrt(xSquared + ySquared)))

# merges two subarrays of prqu
# First subarray is prqu[1..m]
# Second subarray is prqu[m+1..r]
def merge(queue, key, low, high, mid):
    i = low
    j = mid + 1
    temp = []
    # Merge the two halves into temp
    while i <= mid and j <= high:
        if key[queue[i]] < key[queue[j]]:
            temp.append(queue[i])
            i += 1
        else:
            temp.append(queue[j])
            j += 1
    # Push all the remaining values from i to mid into temp
    while i <= mid:
        temp.append(queue[i])
        i += 1
    # Push all the remaining values from j to high into temp
    while j <= high:
        temp.append(queue[j])
        j += 1
    # Assign the sorted data stored from temp to v
    for i in range(low, high+1):
        queue[i] = temp[i-low]

def mergeSort(queue, key, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(queue, key, low, mid)    # sort first half
        mergeSort(queue, key, mid+1, high) # sort second half
        merge(queue, key, low, high, mid)


def MST_Prim(cities):
    key = [sys.maxsize for x in range(len(cities))] # populates a list from 0 to len(cities) with int max
    parent = [None for x in range(len(cities))]     # populates a list from 0 to len(cities) all with None
    queue = [x for x in range(len(cities))]         # populates a list from 0 to len(cities) with numbers 0 to len(cities) to be a priority queue
    key[0] = 0
    mergeSort(queue, key, 0, len(queue) - 1)

    while len(queue) > 0:
        u = queue.pop(0)
        for v in queue:
            dist = EuclideanDistance(cities[u], cities[v])
            if dist < key[v]:
                parent[v] = u
                key[v] = EuclideanDistance(cities[u], cities[v])
                mergeSort(queue, key, 0, len(queue) - 1)
    return parent

def mstToAdjList(mst):
    adjList = OrderedDict()
    for i in range(1, len(mst)):
        if mst[i] in adjList:          # does key mst[i] already exist? Then the list at mst[i] is not empty
            adjList[mst[i]].append(i)  # append vertex v into the list at key mst[i] (vertex u)
        else:                          # append the first vertex into the list at key mst[i]
            adjList[mst[i]] = [i]      # from vertex u to vertex v
    return adjList

def dfs(adjList, cities):
    stack = []
    disc = []
    stack.append(0)  # u = 0, the starting vertex
    disc.append(0)   # u = 0, the starting vertex
    dist = 0
    while len(stack) > 0:
        if stack[len(stack) - 1] in adjList:                        # does key vertex u exist in adjList?
            stack.append(adjList[stack[len(stack) - 1]][0])         # append the first element (vertex v) in the list at key vertex u to the stack
            disc.append(stack[len(stack) - 1])                      # append the vertices in the order they're discovered in
            dist += EuclideanDistance(cities[disc[len(disc)-2]], cities[disc[len(disc)-1]]) # add on top of dist the distance traveled from u to v
            if len(adjList[stack[len(stack) - 2]]) - 1 == 0:        # is the list value at key vertex u empty?
                del adjList[stack[len(stack) - 2]]                  # delete the key/value pair
            else:                                                   # the list value at key vertex u still contains other vertices within it
                del adjList[stack[len(stack) - 2]][0]               # delete the first element in the array at key vertex u
        else:                                                       # vertex u key does not exist in adjList
            stack.pop()                                             # pop vertex u from stack and try a different vertex
    dist += EuclideanDistance(cities[disc[len(disc)-1]], cities[0]) # add on top of dist the distance traveled from u back to the starting vertex
    print(disc)
    print(dist)

def buildAdjMatrix(cities):
    adjMatrix = [[0 for x in range(len(cities))] for y in range(len(cities))]
    for u in range(0, len(cities)):
        for v in range(u + 1, len(cities)):
            ij = EuclideanDistance(cities[u], cities[v])
            adjMatrix[u][v] = ij
            adjMatrix[v][u] = ij
    return adjMatrix

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
    fileName = 'tsp_example_3.txt'
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            city = line.split()
            cities.append([int(city[0]), int(city[1]), int(city[2])])

    mst = MST_Prim(cities)

    adjList = mstToAdjList(mst)

    dfs(adjList, cities)


if __name__ == "__main__":
    main()