from numpy import*
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat = array(mat)
        target = array(target)

        for k in range(4):
            if array_equal(rot90(mat,k),target):
                return True
        return False
        