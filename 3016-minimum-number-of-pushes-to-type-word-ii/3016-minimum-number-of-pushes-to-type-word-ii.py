class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        frequencies = sorted(freq.values(), reverse=True)

        total = 0

        for i, f in enumerate(frequencies):
            position = i // 8 + 1
            total += f * position

        return total
