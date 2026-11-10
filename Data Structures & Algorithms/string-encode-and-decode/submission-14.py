class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string
            res += '~'
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = [""]
        index = 0
        for i in range(len(s) - 1):
            print(index)
            if s[i] != '~':
                res[index] += s[i]
            else:
                index += 1
                res.append("")
        return res
