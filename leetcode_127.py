import collections


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    if endWord not in wordList:
        return 0
    nei = collections.defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)

    # 每一个key是一个不完整的单词，比如h*t, value则是这个h*t可以一步到的在wordlist里的单词
    # 比如hot/hut/hat......

    visited = set()
    q = collections.deque([beginWord])
    steps = 1

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return steps
            for j in range(len(word)):
                #取到当前词可以有的所有pattern。把他们可以一步到的词加到后面去
                pattern = word[:j] + "*" + word[j + 1:]
                for n in nei[pattern]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
        steps += 1
    return steps



