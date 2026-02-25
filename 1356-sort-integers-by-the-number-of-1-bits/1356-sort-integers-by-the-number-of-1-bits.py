class Solution(object):
    def sortByBits(self, arr):
        def swap(arr,a,b):
            temp=arr[a]
            arr[a]=arr[b]
            arr[b]=temp
        
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if (bin(arr[j]).count("1")>bin(arr[j+1]).count("1")) or (bin(arr[j]).count("1")==bin(arr[j+1]).count("1") and arr[j]>arr[j+1]):
                    swap(arr,j,j+1)
        return arr 