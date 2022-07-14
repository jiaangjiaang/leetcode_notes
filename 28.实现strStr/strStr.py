class Solution:
    '''
    def strStr(haystack, needle):
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len > haystack:
            return -1
        if needle_len == haystack:
            if needle == haystack:
                return 0
            else:
                return -1
        if needle_len == 0:
            return 0
    '''
    #用了一个不讲武德的方法
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len > haystack_len:
            return -1
        if needle_len == haystack_len:
            if needle == haystack:
                return 0
            else:
                return -1
        if needle_len == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



            
        
        