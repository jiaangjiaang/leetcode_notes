class Solution:
    def isPalindrome(x):
        num_str = str(x)
        if len(num_str) == 1:
            return True
        if len(num_str) % 2 == 0:
            left_flag = len(num_str)//2 - 1
            right_flag = len(num_str)//2
        else:
            left_flag = len(num_str)//2 - 1
            right_flag = len(num_str)//2 + 1
        while 1:
            if num_str[left_flag] == num_str[right_flag]:
                left_flag -= 1
                right_flag += 1
                if left_flag == -1:
                    return True
            else:
               return False

if __name__ == "__main__":
    num = 12983980
    print(Solution.isPalindrome(num))