class Solution:
    def isValid(s):
        a = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i == "(" or i == "[" or i == "{":
                a.append(i)
            if i == ")":
                if len(a) <= 0:
                    return False
                if a.pop() != "(":
                    return False
            elif i == "]":
                if len(a) <= 0:
                    return False
                if a.pop() != "[":
                    return False
            elif i == "}":
                if len(a) <= 0:
                    return False
                if a.pop() != "{":
                    return False
        if len(a) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "()"
    print(Solution.isValid(s))
