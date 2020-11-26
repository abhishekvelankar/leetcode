#solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x))%2 == 0:
            for i in range(len(str(x))//2):
                if str(x)[i] == str(x)[len(str(x))-1-i]:
                    pass
                else:
                    return False
            return True
        else:
            for i in range((len(str(x))//2)+1):
                if str(x)[i] == str(x)[len(str(x))-1-i]:
                    pass
                else:
                    return False
            return True

#solution 2: we can assume all numbers as odd in that way we will check one extra number all time but can
# eliminate one for loop
class Solution:
    def isPalindrome(self, x: int) -> bool:
        mid = len(str(x))//2
        for i in range(mid+1):
            if str(x)[i] == str(x)[len(str(x))-1-i]:
                pass
            else:
                return False
        return True


