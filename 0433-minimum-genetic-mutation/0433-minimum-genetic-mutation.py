class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = set(start)
        bank = set(bank)
        
        while queue:
            gene, count = queue.popleft()
            if gene == end:
                return count

            for c in "ACGT":
                for i in range(len(gene)):
                    mutation = gene[:i] + c + gene[i + 1:]
                    if mutation not in seen and mutation in bank:
                        queue.append((mutation, count + 1))
                        seen.add(mutation)
                        print(queue)

        return -1