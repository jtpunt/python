# Project: CS 325 Traveling Salesman Problem
# Authors: Jonathan Perry, David Ramirez, Armand Reitz
import math, sys, os
from collections import OrderedDict
from operator import itemgetter

# Returns the Euclidean distance between the two cities, where
# c1[1], c2[1] corresponds with an x-coordinate, and c1[2], c2[2]
# corresponds with an y-coordinate.
def computeDistance(c1, c2):
    xSquared = math.pow(c1[1] - c2[1], 2)
    ySquared = math.pow(c1[2] - c2[2], 2)
    return int(round(math.sqrt(xSquared + ySquared)))

 
def addCities(bins, cities):
    for city in cities:
        bins[city[0]] = city    # key: city_id, value: city_id, x-coord, y-coord

# Explores 3 out of 4 bins (approximately 75% of available cities) at a time to find the next shortest
# path that can be taken. When a shortest path is found, the distance, key, and bin number of the
# corresponding city is saved. Each minimum distance is compared to other city candidates that may be
# the final shortest path that can be taken. Finally, the key of the city along with the bin it resides
# in is returned.
def getNextCity(bins, bin_nums, start, distance):
    minWeight = sys.maxsize
    city_id = 0
    bin_idx = 0
    for bin_num in bin_nums:
        for key, city in bins[bin_num].items():
            dist = computeDistance(start, city)
            if dist < minWeight:
                minWeight = dist
                city_id = key
                bin_idx = bin_num
    distance.append(minWeight)
    return city_id, bin_idx

# Returns the next bins that should be explored based on the current bin of the city just traveled to.
# Because the cities were sorted in ascending order based on their distance from x,y point (0,0),
# we can assume that we only need to look at 3 of the 4 bins that contain cities that are close by.
#   For example: If the current city that was just traveled to was found in bin 1, we should only look at
#   bins 0, 1, and 2 to find the next shortest path. The shortest path would not be found from a city in
#   bin 3, as bin 3 contain cities that are much further away from bin 1.
# The bin of the current city just traveled to should also be the first bin to explore for the next shortest path
# since it contains cities with similar distances from x,y point (0,0)
switcher = {
    0: [0, 1, 3],
    1: [1, 2, 0],
    2: [2, 3, 1],
    3: [3, 0, 2]
}

# Returns the next bins that should be explored based on the current bin of the city just traveled to.
# If the next bins that are going to be explored are empty, return every single bin number. The function
# getNextCity will loop through the empty bins until it finds a bin that contains cities.
def getNextBins(bins, current_bin):
    # get the next bins that should be explored, assuming each bin returned is not empty
    bin_indicies = switcher.get(current_bin, None)
    # check to see if the bin #'s returned contain empty bins
    if len(bins[bin_indicies[0]]) == 0 and len(bins[bin_indicies[1]]) == 0 and len(bins[bin_indicies[2]]) == 0:
        bin_indicies = [0, 1, 2, 3]
    return bin_indicies

# Returns the starting city's city_id, x-coord, y-coord, and the bin it was found in.
def getStartingCity(bins):
    start = []   # will contain the city_id, x-coord, and y-coord
    bin_idx = 0  # will contain the index of the bin that city 11 is found in
    for index, bin in enumerate(bins):
        if 11 in bin: # is the key in the current bin we're looking in?
            start, bin_idx = bin[11], index
            del bin[11] # delete starting city from the bin it's found in
            break
    return start, bin_idx

# Sort cities in ascending order based on their distance from x,y point 0,0, and
# then sort each quarter separately in the list in ascending order based on their city_id.
# etc, a list with 20 cities:
# [1....5] contains city_ids: 5, 7, 8, 11, 12
# [6...10] contains city_ids: 4, 6, 9, 10, 18
# [11..15] contains city_ids: 2, 3, 14, 16, 17
# [16..20] contains city_ids: 1, 13, 15, 19, 20
def sort_cities(cities):
    city = [0, 0, 0]
    cities.sort(key=lambda x: (computeDistance(city, x))) # sort the data in increasing order based on their distance from point 0,0
    quarter = len(cities)//4
    half = len(cities)//2
    cities[: quarter] = sorted(cities[: quarter], key=itemgetter(0))                        # 1st quarter
    cities[quarter: half] = sorted(cities[quarter: half], key=itemgetter(0))                # 2nd quarter
    cities[half: half + quarter] = sorted(cities[half: half + quarter], key=itemgetter(0))  # 3rd quarter
    cities[half + quarter:] = sorted(cities[half + quarter:], key=itemgetter(0))            # 4th quarter

# Greedy Traveling Sales Problem Algorithm: Makes the locally optimum choice at each stage by selecting
# the city nearest to the current city the algorithm is at, as to minimize total distance traveled.
def greedy_tour(table, size, visited_cities):
    start, bin_idx = getStartingCity(table)
    visited_cities.append(start)
    distance = []
    for _ in range(0, size - 1):
        bins = getNextBins(table, bin_idx)
        city_id, bin_idx = getNextCity(table, bins, start, distance)
        visited_cities.append(table[bin_idx][city_id])
        start = table[bin_idx][city_id]
        del table[bin_idx][city_id]
    return sum(distance) + computeDistance(start, visited_cities[0])

# Adds the cities into their bins after they have been first sorted.
# Each bin contains cities that have similar distances from x,y point
# 0,0.
def packBins(cities, bins):
    quarter = len(cities)//4
    half = len(cities)//2
    for _ in range(0, 4): bins.append(OrderedDict())
    addCities(bins[0], cities[: quarter])
    addCities(bins[1], cities[quarter: half])
    addCities(bins[2], cities[half: half + quarter])
    addCities(bins[3], cities[half + quarter:])

def main():
    if len(sys.argv[1:]) != 1:
        print('Only 1 argument needed. Please try again. ')
        quit()
    elif os.path.isfile(sys.argv[1]) is False:
        print("File name not found. Please try again. ")
        quit()
    else:
        fileName = sys.argv[1]

    bins = []            # 4 rows, each containing an orderedDict which contains n/4 items(cities)
    cities = []          # n rows by 3 columns
    visited_cities = []  # n rows by 3 columns

    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            city = line.split()
            cities.append([int(city[0]), int(city[1]), int(city[2])])

    sort_cities(cities)
    packBins(cities, bins)
    distance = greedy_tour(bins, len(cities), visited_cities)

    with open(fileName + '.tour', 'w') as outputFile:
        outputFile.write(str(distance) + '\n')
        for city in visited_cities:
            outputFile.write(str(city[0]) + '\n')

    print("Tour complete.")
if __name__ == "__main__":
    main()