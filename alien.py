"""
Problem 2: Alien Dictionary

Given a sorted list of words from an alien language, determine the character order used in that language.
"""

from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indegree = {char: 0 for word in words for char in word}

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break
        else:
            if len(w2) < len(w1):
                return ""

    queue = deque([char for char in indegree if indegree[char] == 0])
    order = ""

    while queue:
        char = queue.popleft()
        order += char
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(indegree) else ""


if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Expected: wertf")
    print("Output:", alien_order(words))
