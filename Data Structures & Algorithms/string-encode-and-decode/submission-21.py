class Solution:

    def encode(self, strs: List[str]) -> str:
        string = []
        if strs == []:
            return ''
        if strs == [""]:
            return "bruh"
        

        for i in strs:
            # for j in i:
            string.append(i)
        a = "😱".join(string)
        print('encode:', a)

        return a


    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        if s == "bruh":
            return[""]
        print('decode:',s.split())
        return s.split('😱')