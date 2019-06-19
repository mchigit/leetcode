"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Solution:

Visualize word in the wordList as nodes in a graph, so we are basically performing a BFS
To find the shortest path between starting and endword
We can use bidirectional BFS to speed up the process
"""

from queue import Queue
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #    Code below doesn't use bidirectional BFS
        #         if endWord not in wordList:
        #             return 0

        #         q = Queue()
        #         step = 0
        #         q.put(beginWord)

        #         while not q.empty():
        #             step += 1
        #             size = q.qsize()
        #             for _ in range(size):
        #                 word = q.get()
        #                 for i in range(len(word)):
        #                     for c in ascii_lowercase:
        #                         if c == word[i]:
        #                             continue
        #                         newWord = list(word)
        #                         newWord[i] = c
        #                         newStr = "".join(newWord)
        #                         if newStr == endWord:
        #                             return (step + 1)
        #                         elif newStr not in wordList:
        #                             continue
        #                         else:
        #                             q.put(newStr)

        #         return 0
        wordDict = set(wordList)
        if endWord not in wordDict: return 0

        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for w in s1:
                new_words = [
                    w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(l)]
                for new_word in new_words:
                    if new_word in s2: return step + 1
                    if new_word not in wordDict: continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0