class Solution:
    def maximum69Number (self, num: int) -> int:
        l=list(map(int,str(num)))
        for i in range(len(l)):
            if l[i]==6:
                l[i]=9
                break
        return int(''.join(map(str,l)))

        