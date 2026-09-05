class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]

                    if new_word == endWord:
                        return steps + 1

                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, steps + 1))

        return 0
