class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        frequencies = sorted(freq.values(),reverse=True)

        total_pushes = 0

        for i,f in enumerate(frequencies):
            position = (i//8)+1
            total_pushes+=f*position
        
        return total_pushes

        