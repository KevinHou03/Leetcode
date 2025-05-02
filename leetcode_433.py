from collections import deque


def minMutation(startGene, endGene, bank):
    """
    :type startGene: str
    :type endGene: str
    :type bank: List[str]
    :rtype: int
    """

    if endGene not in bank:
        return -1

    visited = {startGene}
    genes = ['T','C','G','A']

    queue = deque([(startGene, 0)])
    while queue:
        cur_gene, step = queue.popleft()
        if cur_gene == endGene:
            return step

        for i in range(len(cur_gene)):
            for g in genes:
                if g != cur_gene[i]:
                    new_gene = cur_gene[:i] + g + cur_gene[i + 1:]

                    if new_gene not in visited and new_gene in bank:
                        visited.add(new_gene)
                        queue.append((new_gene, step + 1))
    return -1
