class Solution:
    def bruh(self, bruh):
        return bruh[1]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        finallist = []
        bucket = [[] for i in range(len(nums) + 1)]
        for key, values in count.items():
            bucket[values].append(key)
        # print('counter:', count)
        # print('bucket:', bucket)
        # maxx = max(bucket) 
        # print(maxx)
        rev_bucket = bucket[::-1]
        # print(rev_bucket)
        for row in rev_bucket:
            for val in row:
                if len(finallist) != k:
                    finallist.append(val)
        return finallist
        # a = list(count.items())
        # b = sorted(a, key=self.bruh, reverse = True)
        # finallist = []
        # for i in range(k):
        #     finallist.append(b[i][0])
        # return finallist