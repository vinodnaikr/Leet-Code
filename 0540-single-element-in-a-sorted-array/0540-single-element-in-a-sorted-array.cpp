class Solution {
public:
    int singleNonDuplicate(vector<int>& arr) {
        int st=0;
        int n = arr.size();
        int end = arr.size()-1;

        while(st<=end){
            int mid = st+(end-st)/2;

            if (n==1){
                return arr[0];
            }

            if(mid == 0 && (arr[0]!=arr[1])){
                return arr[mid];
            }

            if(mid == end && (arr[n-1] != arr[n-2])){
                return arr[mid];
            }

            if(arr[mid-1]!=arr[mid] && arr[mid]!=arr[mid+1]){
                return arr[mid];
            }

            if(mid%2 == 0){
                if(arr[mid-1] == arr[mid]){
                    end = mid-1;
                }
                else{
                    st = mid+1;
                }
            }
            else{
                if(arr[mid-1] == arr[mid]){
                    st = mid+1;

                }
                else{
                    end = mid-1;
                }
            }
        }
        return -1;
        
    }
};