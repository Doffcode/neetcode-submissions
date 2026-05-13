class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        //find the length of string with minimum length  
        string ret="";
        int min =INT_MAX;
        for(int i=0 ; i< strs.size(); i++)
        {
            if (strs[i].size() <min)
            min=strs[i].size();
        }
        // loop from 0 to min and check the matching character
        for(int i=0; i<min; i++)
        {
            //loop from 0 to strs.size() to match the chracters of every string 
            int flag =0;
            for(int j=1; j<strs.size();j++)
            {
                char c=strs[0][i];
                cout<<c<<" this is equal to "<<strs[j][i]<<endl;
                if( strs[j][i]!= c)
                {
                flag++;
                break;
                }
            }
            if(flag>0)
            {
                return ret;
            }
            else if (flag==0)
            {
                //cout<<strs[0].at(i)<<endl;
                ret.push_back(strs[0].at(i));
            }
        }
        return ret;
        
    }
};