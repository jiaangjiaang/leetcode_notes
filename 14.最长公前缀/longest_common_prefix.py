class Solution:
    def longest_common_prefix(self, strs):
        if not strs:
            return ''
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix


    def lcp(self, prefix, str2):
        length, index = min(len(prefix), len(str2)), 0
        while index < length and prefix[index] == str2[index]:
            index += 1

        return prefix[:index]

if __name__ == "__main__":
    strs = ["cir","car"]
    print(Solution.longest_common_prefix(strs))