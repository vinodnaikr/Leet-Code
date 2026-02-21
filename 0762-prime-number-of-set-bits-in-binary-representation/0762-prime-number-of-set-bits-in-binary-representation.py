class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(n):
            if n<=1:
                return False
            for i in range(2,n):
                if n%i==0:
                    return False
            return True

        count=0
        for i in range(left,right+1):
            no_of_bits=bin(i).count("1")
            if is_prime(no_of_bits)==True:
                count+=1
        return count

