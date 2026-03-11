class Solution(object):
    def bitwiseComplement(self, n):
        binary_complement=[]
        binary=bin(n)[2:]

        for i in range(len(binary)):
            if binary[i]=='1':
                binary_complement.append('0')
            else:
                binary_complement.append('1')

        binary_comp_str=''.join(binary_complement)
        comp_integer=int(binary_comp_str,2)

        return comp_integer
