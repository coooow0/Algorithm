class Solution(object):
    def numberOfSteps(self, num):
        obtain = num
        i = 0
        while obtain > 0:
            if obtain % 2 == 0:
                obtain //= 2
            else:
                obtain -= 1
            i += 1
    
        return i