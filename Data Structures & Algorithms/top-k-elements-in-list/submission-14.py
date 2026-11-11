class Solution:
    def bruh(self, bruh):
        return bruh[1]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # print('counter:', count)
        # print('a:', a)
        a = list(count.items())
        b = sorted(a, key=self.bruh, reverse = True)
        finallist = []
        for i in range(k):
            finallist.append(b[i][0])
        return finallist