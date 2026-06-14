# Problem 875: Koko Eating Bananas
# Difficulty: Medium
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Language: cpp
# ────────────────────────────────────────

class Solution {
public:
    int maximumElement(vector<int>& piles){
        int maxi=INT_MIN;
        for(auto itt: piles){
            maxi=max(maxi,itt);
        }
        return maxi;
    }
    long long minimumHours(vector<int>& piles,int mid){
        long long newvalue=0;
        for(auto itt:piles){
            newvalue+=ceil(double(itt)/double(mid));
        }
        return newvalue;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low=1;
        int high=maximumElement(piles);
        while(low<=high){
            int mid=low+(high-low)/2;
            long long newval=minimumHours(piles,mid);
            if(newval<=h){
                high=mid-1;
            }
            else {
                low=mid+1;
            }
        }
        return low;
    }
};