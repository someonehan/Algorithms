# A strobogrammatic number is a number that looks the same rotated 180
# degrees(looked at upside and down)
# find all strobogrammatic that are of length = 0
#For example,
# Given n = 2, return ["11","69","88","96"].
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

class Solution:
    lookup = {"0": '0', "1": '1', "8": '8', "6": '9', "9": '6'}

    def strobogrammatic_nums(self, length):
        if length == 0:
            return ['']
        if length == 1:
            return ['0', '1', '8']
        ret = []
        for num in self.strobogrammatic_nums(length - 2):
            for k, v in self.lookup.items():
                ret.append(''.join([k, num, v]))
        ret = [item for item in ret if not item.startswith('0')]
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.strobogrammatic_nums(3))



