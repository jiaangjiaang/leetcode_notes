class Solution:
    def isAnagram(s, t):
        if len(s) > len(t):
            return False
        s_dict = {}
        for s_str in s:
            s_dict[s_str] = s_dict.get(s_str, 0) + 1

        for t_str in t:
            if t_str not in s_dict:
                return False
            else:
                s_dict[t_str] -= 1
        m = list(s_dict.values())
        if len(s) == len(t) and m.count(0) == len(s_dict.keys()):
            return True
        else:
            return False