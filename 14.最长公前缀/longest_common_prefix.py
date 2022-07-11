class Solution:
    def longest_common_prefix(strs):
        lens = len(strs)
        result = ""
        dict = {}
        for i in strs[0]:
            dict[i] = 1
        for j in range(1, lens):
            for k in strs[j]:
                if k in dict.keys():
                    dict[k] += 1
        for key, value in dict.items():
            if value == lens:
                result += key
            else:
                return result
        return result


if __name__ == "__main__":
    strs = ["aa", "aa", "aa"]
    print(Solution.longest_common_prefix(strs))