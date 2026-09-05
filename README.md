# LeetCode 127 – Word Ladder

## Problem

Given two words, `beginWord` and `endWord`, and a dictionary of words, find the **length of the shortest transformation sequence** from `beginWord` to `endWord`.

A valid transformation follows these rules:

* Only one letter can be changed at a time.
* Every transformed word must exist in the word list.
* The sequence starts with `beginWord`.
* The sequence ends with `endWord`.

If no valid transformation exists, return `0`.

## Example 1

**Input:**

```text
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
```

**Output:**

```text
5
```

One shortest transformation is:

```text
hit → hot → dot → dog → cog
```

The sequence contains 5 words.

## Example 2

**Input:**

```text
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
```

**Output:**

```text
0
```

The `endWord` `"cog"` is not present in the word list, so no valid transformation is possible.

## Approach

This problem can be treated as a **graph traversal** problem.

Each word represents a node, and two words are connected when they differ by exactly one character.

Since we need the **shortest transformation sequence**, **Breadth-First Search (BFS)** is the natural approach.

BFS explores all words at the current transformation level before moving to the next level. Therefore, when `endWord` is reached for the first time, the number of levels represents the shortest sequence length.

## Algorithm

1. Check whether `endWord` exists in the word list.
2. Add the words to a set for fast lookup.
3. Start BFS with `beginWord`.
4. For each word:

   * Change each character to every possible lowercase letter.
   * Check whether the resulting word exists in the dictionary.
5. Add valid and unvisited words to the BFS queue.
6. Increase the transformation level after processing each level.
7. If `endWord` is reached, return the current sequence length.
8. If the queue becomes empty without reaching `endWord`, return `0`.

## Complexity

Let `N` be the number of words and `L` be the length of each word.

* **Time Complexity:** `O(N × L × 26)`
  Each word may be checked by changing every character to 26 possible letters.

* **Space Complexity:** `O(N)`
  The word set and BFS queue can contain up to `N` words.

## Key Learning

This problem is a good example of using **BFS to find the shortest path in an unweighted graph**.

It also demonstrates how a word transformation problem can be converted into a graph problem, where each valid word is treated as a node.

## LeetCode Details

* **Problem Number:** 127
* **Problem Name:** Word Ladder
* **Difficulty:** Hard
* **Language:** Python 3
* **File:** `solution.py`

## Topics

* Hash Table
* String
* Breadth-First Search

## Author

T.Nandhini
