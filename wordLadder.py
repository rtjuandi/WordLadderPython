from collections import defaultdict
from collections import deque

# Raydi Tjuandi
# Word Ladder

# Global Variables
minLen =  4
maxLen = 6

# Function that builds the dictionary graph
def buildGraph(file):
    buckets = defaultdict(list)
    graph = defaultdict(set)
    f = open(file, 'r')

    # Goes through every line in dictionary.txt
    for line in f:
        word = line[:-1]

        # Requirement check
        if(len(word) >= minLen and len(word) <= maxLen):
            
            for i in range(len(word)):
                # Creates wild card for word
                bucket = word[:i] + "-" + word[i+1:]
                buckets[bucket].append(word)

    for key in buckets:
        for w1 in buckets[key]:
            for w2 in buckets[key]:
                if w1 != w2:
                    graph[w1].add(w2)
                    graph[w2].add(w1)
    return graph

# Function that does the bfs traversal
def bfs(graph, start, end):
    #keep track of what is visited
    visited = set()

    #bfs uses a queue
    q = deque([[start]])

    # Goes through all possible paths for a word ladder from the starting word until target word is found
    while(q):
        p = q.popleft()

        for nxt in graph[p[-1]] - visited:
            visited.add(nxt)
            q.append(p + [nxt])

        # If ladder is found that matches the end, loop breaks
        if(p[0] == start and p[-1] == end):
            return p

    # Else, continue traversing and if nothing is foudn return this
    return "No Ladders Found."


# Function that reads pair.txt and prints out the ladder if it is found
def processFile(infile, graph):
    f = open(infile, 'r')

    for line in f:
        line = line.rstrip()
        words = line.split(" ")

        start = words[0];
        end = words[-1];

        print(start)
        print(end)

        # Requirement checking
        if(len(start) != len(end) or ( (len(start) < minLen or len(end) < minLen) or (len(start) > maxLen or len(end) > maxLen))):
            print("Requirements not met. No Ladders Found.")

        else:
            print(bfs(graph, words[0], words[-1]));

        print(" ")
        

def main():
    wordGraph = buildGraph("dictionary.txt")
    processFile("pairs.txt", wordGraph)



if __name__ == "__main__":
    main()
