class Solution:
    # def bullshit(self, string):
    #     seen = {}
    #     for char in string:
    #         if char in seen:
    #             seen[char] += 1
    #         else:
    #             seen[char] = 1
    #     return[seen]

    # {a:1, c:1, t:1} 
    # {p:1, o:1, t:1, s:1}

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        listt = []


        for i, string in enumerate(strs):
            s = ''.join(sorted(string))
            # s = act, pots, pots, act, pots, hat

            if s in seen:
                seen[s].append(string)
                # seen = {'act':0, 'pots':1 ...} 
                # if sorted string is in seen, append it to it.
            else: # NOT in seen
                seen[s] = []
                seen[s].append(string) 
                # print(seen)
                # seen = {'act':0, 'pots':1 ...} 
                # sorted string is stored as the key. and values are appended when s in seen


        for i in seen.values():
            listt.append(i) 
        return listt





        # Failed approach by using counter
        # temp = {}
        # for i, num in enumerate(strs):
        #     temp[Counter(num)] = i
        # print(temp)
        # return []

            