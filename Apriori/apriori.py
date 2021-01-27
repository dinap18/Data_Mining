"""
Dina Pinchuck
Liel Orenstein
"""


import random
from collections import defaultdict
from itertools import chain, combinations
N = 5  # no. of attributes
MINSUP = 0.4  # min percent


# Creates a file named filename containing m sorted itemsets of items 0..N-1
def createfile(m, filename):
    f = open(filename, "w")  # opens file for writing
    for line in range(m):  # m in number of lines in the file
        itemset = []
        for i in range(random.randrange(N) + 1):
            item = random.randrange(N)  # random integer 0..N-1
            if item not in itemset:
                itemset += [item]
        itemset.sort()
        for i in range(len(itemset)):
            f.write(str(itemset[i]) + " ")
        f.write("\n")
    f.close()


# Returns true if all of smallitemset items are in bigitemset (the itemsets are sorted lists)
def is_in(smallitemset, bigitemset):
    s = b = 0  # s = index of smallitemset, b = index of bigitemset
    while s < len(smallitemset) and b < len(bigitemset):
        if smallitemset[s] > bigitemset[b]:
            b += 1
        elif smallitemset[s] < bigitemset[b]:
            return False
        else:
            s += 1
            b += 1
    return s == len(smallitemset)


# Returns a list of itemsets (from the list itemsets) that are frequent
# in the itemsets in filename
def frequent_itemsets(filename, itemsets):
    f = open(filename, "r")
    filelength = 0  # filelength is the no. of itemsets in the file. we
    # use it to calculate the support of an itemset
    count = [0] * len(itemsets)  # creates a list of counters
    line = f.readline()
    while line != "":
        filelength += 1
        line = line.split()  # splits line to separate strings
        for i in range(len(line)):
            line[i] = int(line[i])  # converts line to integers
        for i in range(len(itemsets)):
            if is_in(itemsets[i], line):
                count[i] += 1
        line = f.readline()
    f.close()
    freqitemsets = []
    for i in range(len(itemsets)):
        if count[i] >= MINSUP * filelength:
            freqitemsets += [itemsets[i]]

    return freqitemsets

def create_kplus1_itemsets(kitemsets, filename,n):
    sets = []
    helpSet=[]
    for i in kitemsets:
        if len(i) == n:
            sets.append(set(i))
        helpSet.append(set(i))
    kplus1_itemsets = []
    for i in range(len(sets)-1):
        for j in range(i+1,len(sets)):
            check = sets[i].union(sets[j])
            if len(check) == n+1 and powersets(check,helpSet):
                kplus1_itemsets.append(list(check))

    return frequent_itemsets(filename, kplus1_itemsets)

def powersets(sets,lst):
    for z in chain.from_iterable(combinations(sets, r) for r in range(1,len(sets))):
        if set(z) not in lst:
            return False
    return True


def create_1itemsets(filename):
    it = []
    for i in range(N):
        it += [[i]]
    return frequent_itemsets(filename, it)

def minsup_itemsets(filename):
    minsupsets = kitemsets = create_1itemsets(filename)
    n=1
    while kitemsets != []:
        kitemsets = create_kplus1_itemsets(kitemsets, filename,n)
        minsupsets += kitemsets
        n+=1
    return support(minsupsets)

def support(freq):
    sets = []
    for i in freq:
        sets.append(set(i))
    count=defaultdict(int)
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i].issubset(sets[j]):
                count[tuple(sets[i])] += 1
        count[tuple(sets[i])] += 1
    for i in range(len(freq)):
        freq[i].append(count[tuple(freq[i])])
    return freq


createfile(100, "itemsets.txt")
print(minsup_itemsets("itemsets.txt"))




