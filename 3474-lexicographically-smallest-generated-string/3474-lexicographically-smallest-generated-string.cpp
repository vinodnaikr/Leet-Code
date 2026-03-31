class Solution {
public:
    string generateString(string str1, string str2) {
        int n=str1.length();
        int m=str2.length();
        int L=n+m-1;

        vector<char> word(L,'\0');

        for(int i=0;i<n;i++){
            if(str1[i]=='T'){
                for(int j=0;j<m;j++){
                    int pos=i+j;
                    if(word[pos]!='\0' && word[pos]!=str2[j]){
                        return "";
                    }
                    word[pos]=str2[j];
                }
            }
        }

        vector<bool> free(L,false);
        for(int i=0;i<L;i++){
            if(word[i]=='\0'){
                word[i]='a';
                free[i]=true;
            }
        }

        for(int i=0;i<n;i++){
            if(str1[i]=='F'){
                bool matches=true;
                for(int j=0;j<m;j++){
                    if(word[i+j]!=str2[j]){
                        matches=false;
                        break;

                    }
                }
                if(matches){
                    bool fixed=false;
                    for(int j=m-1;j>=0;j--){
                        int pos=i+j;
                        if(free[pos]){
                            word[pos]='b';
                            free[pos]=false;
                            fixed=true;
                            break;
                        }
                    }
                    if(!fixed){
                        return "";
                    }

                }

            }

        }
        for(int i=0;i<n;i++){
            if(str1[i]=='F'){
                bool matches=true;
                for(int j=0;j<m;j++){
                    if(word[i+j]!=str2[j]){
                        matches=false;
                        break;
                    }
                }
                if(matches){
                    return "";
                }

            }

        }
        string result(word.begin(),word.end());
        return result;
    }
};