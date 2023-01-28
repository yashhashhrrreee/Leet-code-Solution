class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0,h=nums.size()-1;
        while(l<=h){
            int mid=(l+h)>>1;
            if(nums[mid]==target) return mid; // when we found the target 
            if(nums[l]<=nums[mid]){ // if selected part is  sorted 
                if(target>=nums[l]&& target<=nums[mid]) // checking if target lies in l-mid
                    h=mid-1;
                else
                    l=mid+1;
            }
            else{
                if(target>=nums[mid]&& target<=nums[h])// checking if target lies in mid-h
                    l=mid+1;
                else 
                    h=mid-1;
            }
        }
        return -1; // when target not found
    }
};