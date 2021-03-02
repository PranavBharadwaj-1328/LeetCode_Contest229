#Driver code was given by the platform
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out = []
        for i in range(len(boxes)):
            s1 = 0
            s2 = 0
            for j in range(0,i):
                if(boxes[j] == '1'):
                    s1 += i-j
            for k in range(i+1,len(boxes)):
                if(boxes[k] == '1'):
                    s2 += k-i
            out.append(s1+s2)
        return out
