class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = dict(Counter(word))
        frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        clicks = 0
        place = 0
        for key, value in frequency.items():
            clicks = clicks + value*((place//8)+1)
            place+=1
        return clicks
